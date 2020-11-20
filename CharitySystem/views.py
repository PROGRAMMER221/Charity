from django.shortcuts import render, redirect, get_object_or_404
from .forms import NGO_form , donation_form
from .models import NGO, donation_request, donation_history
from django.contrib import messages
from django.core.mail import send_mail
import stripe
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
stripe.api_key = 'sk_test_TjwJ8KIE4pM0zUDkkubD4kvV00PipgfR59'

def header(request):
    return render(request, 'CharitySystem/header.html')

def about(request):
    return render(request, 'CharitySystem/self.html')

@login_required
def ngo(request):
    if request.method == 'POST':
        form = NGO_form(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            send_mail(
                'SaathiHaathBadhana | Verification Status',
                'Our Admins Have Recived Your Request and will be verified through legal means and will be processed within 24 to 48 hrs. Please Be patient',
                'aman_22@outlook.com',
                [email],
                fail_silently=False,
            )
            return redirect('/')
    else:
        form = NGO_form()

    return render(request,"CharitySystem/get_verified.html",{'form':form})

@login_required
def not_verified(request):
    return render(request, "CharitySystem/not_verified.html")

@login_required
def verify_from_admin(request):
    if request.user.is_superuser is False:
        return redirect('/404_admin/')
    data = NGO.objects.all()
    return render(request, "CharitySystem/verify_from_admin.html", {'ngo':data})

def Verification_Status_True(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    ngo.verification_true()

    send_mail(
    'SaathiHaathBadhana | Verification Status',
    'Our admins have deemed your verification to be right.',
    'aman_22@outlook.com',
    [ngo.email],
    fail_silently=False,
    html_message=render_to_string("CharitySystem/mail_Y.html")
)

    return redirect("/admin_verify/")

def Verification_Status_False(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    ngo.verification_false()

    send_mail(
    'SaathiHaathBadhana | Verification Status',
    'Our admins have deemed your verification to be wrong.',
    'aman_22@outlook.com',
    [ngo.email],
    fail_silently=False,
    html_message=render_to_string("CharitySystem/mail_N.html")
)
    print(ngo.email)
    return redirect("/admin_verify/")

# def mail_Y(request):
#     send_mail(
#     'SaathiHaathBadhana | Verification Status',
#     'Our admins have deemed your verification to be wrong.',
#     'aman_22@outlook.com',
#     ['heroup534@gmail.com'],
#     fail_silently=False,
#     html_message=render_to_string("CharitySystem/mail_Y.html")
# )
#     return render(request, "CharitySystem/mail_Y.html")

# def mail_N(request):
#     html_content = render_to_string('CharitySystem/mail_N.html')
#     text_content = strip_tags(html_content)

#     email = EmailMultiAlternatives(
#         'SaathiHaathBadhana | Verification Status',
#         text_content,
#         'aman_22@outlook.com',
#         ['nepoxes673@0335g.com']
#     )
#     email.attach_alternative(html_content, 'text/html')
#     email.send()

#     return render(request, "CharitySystem/mail_N.html")

def donation(request):
    try:
        ngo = NGO.objects.get(ngo_current_user=request.user)
        if ngo.verification_status is True:
            if request.method == 'POST':
                form = donation_form(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('/')
            else:
                form = donation_form()

            return render(request, "CharitySystem/request_form.html",{'form':form})
        else:
            messages.error(request,'Your NGO is Not Authenticated !!')
            return redirect('/')

    except ObjectDoesNotExist:
        return redirect('/404/')

def post_request(request):
    cursor = connection.cursor()
    cursor.execute('SELECT ngo_name, head_of_ngo, contactNo, donation_description, donation_amount FROM CharitySystem_NGO INNER JOIN CharitySystem_donation_request on CharitySystem_donation_request.donation_request_user = CharitySystem_NGO.ngo_current_user;')
    row = cursor.fetchall()

    context = {
        'row' : row
    }
    print(row)
    return render(request, "CharitySystem/post_request.html", context)

def payment(request):
    context = {
        'ngo' : NGO.objects.all()
    }
    return render(request, 'CharitySystem/payment.html', context)

def charge(request):
    his = donation_history()
    if request.method == 'POST':

        cus_name = request.POST["cus_name"]
        amount = request.POST["amount"]
        doantion_message = request.POST["message"]
        mail = request.POST["mail"]
        term = request.POST['terms']
        donateto = request.POST['donateTO']

        customer = stripe.Customer.create(
            email = mail,
            name = cus_name,
            source = request.POST["stripeToken"]
        )

        charge = stripe.Charge.create (
            customer = customer,
            amount = int(amount)*100,
            currency = 'INR',
            description = doantion_message
        )
        his.donar_name = cus_name
        his.donatedTO = donateto
        his.when = timezone.now()
        his.amount = amount
        his.terms = term
        his.save()

        return render(request, 'CharitySystem/success_payment.html',{'amount':amount})

def View404(request):
    return render(request,'CharitySystem/404.html')

def Admin404(request):
    return render(request,'CharitySystem/404_admin.html')

def DonationHistroyView(request):
    if request.user.is_superuser :
        context = {
            'don_his' : donation_history.objects.all()
        }
    else:
        context = {
            'don_his' : donation_history.objects.filter(current_donor=request.user)
        }

    return render(request, 'CharitySystem/history.html', context)