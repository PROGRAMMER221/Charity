from django.contrib import admin
from .models import NGO, donation_request, donation_history

# Register your models here.

admin.site.register(NGO)

admin.site.register(donation_request)

admin.site.register(donation_history)