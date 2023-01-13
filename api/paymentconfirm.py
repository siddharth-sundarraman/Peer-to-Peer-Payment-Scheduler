from django.conf import settings
from django.core.mail import send_mail

def send_payment_confirmation_email(payment_instance):

    send_mail(
        'Stripe Payment Confirmation',
        f'You have successfully sent {payment_instance.amount} to {payment_instance.recipient_email}',
        'paymentscheduler1526@gmail.com',
        [f'{payment_instance.user.email}'],
        fail_silently=False
    )