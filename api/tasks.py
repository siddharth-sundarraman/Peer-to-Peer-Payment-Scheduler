from .paymentconfirm import send_payment_confirmation_email
from .models import PaymentInstance, Payment
from .keys import stripe_secret_key
from datetime import datetime

from celery import shared_task
from .models import PeriodicTask


import stripe

@shared_task
def create_recurring_payment(payment_instance_id):

    print('Test to see if task ran')

    payment_instance = PaymentInstance.objects.get(id=payment_instance_id)

    if payment_instance.end_date and payment_instance.end_date < datetime.now().date():

        PeriodicTask.objects.filter(name=f'task_name_{payment_instance_id}').delete()
        
    stripe.api_key = stripe_secret_key
    

    recipient = payment_instance.recipient_stripe_id or payment_instance.recipient_email

    try:
        account = stripe.Account.retrieve(recipient)
    except stripe.error.InvalidRequestError:
        account = stripe.Account.create(email=recipient)

    destination = account.id
   


    payment_intent = stripe.PaymentIntent.create(
        payment_method = payment_instance.payment_method.stripe_payment_method_id,
        amount = payment_instance.amount,
        currency = 'usd',
        description = payment_instance.title,
        capture_method = 'automatic',
        confirm = True,
        off_session = True,
        on_behalf_of = payment_instance.payment_method.stripe_account_id,
        transfer_data = {
            'destination': destination,
        },
    )

    payment = Payment(
        user = payment_instance.user,
        payment_instance = payment_instance,
        recipient_email = payment_instance.recipient_email,
        amount = payment_instance.amount,
        status = payment_intent.status,
        title =  payment_instance.title,
    )
    
    payment.save()
    
    send_payment_confirmation_email(payment_instance)