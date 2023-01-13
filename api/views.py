from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import PaymentMethod, PaymentInstance, Payment
from .serializers import PaymentMethodSerializer, PaymentInstanceSerializer, PaymentSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def endpoints(request):
    endpoints = {
            'PaymentMethod list': '/paymentmethods/',
            'PaymentMethod detail': '/paymentmethods/<int:pk>',
            'PaymentInstance list': '/paymentinstances/',
            'PaymentInstance detail': '/paymentinstances/<int:pk>',
            'Payment list': '/payments/',
            'Payment detail': '/payments/<int:pk>',
        }
    return Response(endpoints)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def paymentMethodList(request):

    if request.method == 'GET':
        paymentMethods = PaymentMethod.objects.filter(user=request.user)
        serializer = PaymentMethodSerializer(paymentMethods, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PaymentMethodSerializer(data = request.data, context={'user': request.user})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def paymentMethodDetail(request, pk):

    try:
        paymentMethod = PaymentMethod.objects.get(pk=pk)
    except PaymentMethod.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentMethodSerializer(paymentMethod, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PaymentMethodSerializer(paymentMethod, data = request.data, partial=True, context={'user': request.user})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        paymentMethod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def paymentList(request):
    payments = Payment.objects.filter(user=request.user)
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def paymentDetail(request, pk):

    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentSerializer(payment, many=False)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def paymentInstanceList(request):

    if request.method == 'GET':
        paymentInstances = PaymentInstance.objects.filter(user=request.user)
        serializer = PaymentInstanceSerializer(paymentInstances, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PaymentInstanceSerializer(data = request.data, context={'user': request.user})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def paymentInstanceDetail(request, pk):

    try:
        paymentInstance = PaymentInstance.objects.get(pk=pk)
    except PaymentInstance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentInstanceSerializer(paymentInstance, many=False)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        paymentInstance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)