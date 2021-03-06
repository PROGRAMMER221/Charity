from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.header, name="header"),
    url(r'^self/$', views.about, name="about"),
    url(r'^get_verified/$', views.ngo, name="ngo"),
    url(r'^not_verified/$', views.not_verified, name="not_verified"),
    url(r'^admin_verify/$', views.verify_from_admin, name="verification_from_admin"),
    url(r'^verified_as_true/(?P<pk>\d+)/$',views.Verification_Status_True, name="verified_as_true"),
    url(r'^verified_as_false/(?P<pk>\d+)/$',views.Verification_Status_False, name="verified_as_false"),
    url(r'^post_request/$', views.post_request, name="post_request"),
    url(r'^fund_request/$', views.donation,name="fund request"),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^charge/$', views.charge, name="charge"),
    url(r'^404/$', views.View404, name='404'),
    url(r'^404_admin/$', views.Admin404, name='404_admin'),
    url(r'^donation_history/$',views.DonationHistroyView, name='donation_history'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)