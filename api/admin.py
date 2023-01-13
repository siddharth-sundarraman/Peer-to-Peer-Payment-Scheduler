from django.contrib import admin
from .models import PaymentInstance, Payment, PaymentMethod
# Register your models here.

admin.site.register(PaymentMethod)
admin.site.register(PaymentInstance)
admin.site.register(Payment)