from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time
from django.core.exceptions import ValidationError

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from celery.result import AsyncResult
import json



# Create your models here.

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_account_id = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    stripe_payment_method_id = models.CharField(max_length=200, null=True)

class PaymentInstance(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    recipient_email = models.EmailField()
    recipient_stripe_id = models.CharField(max_length=200, null=True)
    amount = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-start_date',)

    def save(self, *args, **kwargs):

        if self.start_date < datetime.now().date():
            raise ValidationError("Start date cannot be in the past")
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

        super(PaymentInstance, self).save(*args,**kwargs)

        if self.pk is None:

            schedule, _ = CrontabSchedule.objects.get_or_create(
            month_of_year='*/1',
            day_of_month=self.start_date.day,
            hour='0',
            minute='0',
            )

            PeriodicTask.objects.create(
                crontab=schedule,
                name=f'task_name_{self.id}',
                task='create_recurring_payment',
                args=json.dumps([self.id]),
            )


    def delete(self, *args, **kwargs):
        
        super(PaymentInstance, self).delete(*args, **kwargs)

        if self.pk:
            PeriodicTask.objects.filter(name=f'task_name_{self.id}').delete()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    payment_instance = models.ForeignKey(PaymentInstance, on_delete=models.SET_NULL, null=True)
    recipient_email = models.EmailField()
    amount = models.PositiveIntegerField( )
    status = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)