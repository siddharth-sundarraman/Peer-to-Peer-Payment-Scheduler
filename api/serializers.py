from rest_framework import serializers

from .models import Payment, PaymentInstance, PaymentMethod, User

class PaymentMethodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PaymentMethod
        fields = ['id', 'stripe_account_id', 'title', 'stripe_payment_method_id']

    def create(self, validated_data):
        user = self.context['user']
        payment_method = PaymentMethod(**validated_data, user=user)
        payment_method.save()
        return payment_method
    
class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'payment_instance', 'recipient_email', 'amount', 'status', 'title', 'date']

class PaymentInstanceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = PaymentInstance
        fields = ['id', 'title', 'recipient_email', 'recipient_stripe_id', 'payment_method', 'amount', 'start_date', 'end_date']

    def create(self, validated_data):
        user = self.context['user']
        payment_instance = PaymentInstance(**validated_data, user=user)
        payment_instance.save()
        return payment_instance