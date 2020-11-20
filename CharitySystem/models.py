from django.db import models
from django_currentuser.middleware import get_current_user, get_current_authenticated_user

class NGO(models.Model):
    ngo_name = models.CharField(max_length=30,blank=True)
    domain = models.CharField(max_length=20,blank=True)
    head_of_ngo = models.CharField(max_length=30,blank=True)
    contactNo = models.CharField(max_length=10,blank=True)
    email = models.EmailField(blank=True)
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200, blank=True)
    state = models.CharField(max_length=50)
    country= models.CharField(max_length=50)
    registration_cerificate_Trust_Society = models.FileField(upload_to='verification',blank=True)
    certificate_12A = models.FileField(upload_to='verification',blank=True)
    beneficiary_profiles = models.FileField(upload_to='verification',blank=True)
    verification_status = models.NullBooleanField(default=None,blank=True,null=True)
    ngo_current_user = models.CharField(default=get_current_authenticated_user,blank=True,max_length=40)

    def verification_true(self):
        self.verification_status=True        
        self.save()

    def verification_false(self):
        self.verification_status = False
        self.save()

    def __str__(self):
        return self.ngo_name


class donation_request(models.Model):
    donation_description = models.TextField(blank=True,default=None)
    donation_amount = models.CharField(default=None,blank=True,max_length=15)
    donation_request_user = models.CharField(blank=True,default=get_current_authenticated_user,max_length=30)

    def __str__(self):
        return self.donation_amount

class donation_history(models.Model):
    donar_name = models.CharField(max_length=50)
    donatedTO = models.CharField(max_length=100)
    when = models.DateTimeField()
    amount = models.IntegerField()
    terms = models.BooleanField(default=False)
    current_donor = models.CharField(default=get_current_authenticated_user,max_length=50)

    def __str__(self):
        return self.donar_name