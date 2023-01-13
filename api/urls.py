from django.urls import path
from . import views



urlpatterns = [
    path('', views.endpoints, name="endpoints" ),
    path('paymentmethods/', views.paymentMethodList, name="payment-method-list" ),
    path('paymentmethods/<int:pk>/', views.paymentMethodDetail, name="payment-method-detail"),
    path('payments/', views.paymentList, name="payment-list" ),
    path('payments/<int:pk>/', views.paymentDetail, name="payment-detail"),
    path('paymentinstances/', views.paymentInstanceList, name="payment-instance-list" ),
    path('paymentinstances/<int:pk>/', views.paymentInstanceDetail, name="payment-instance-detail"),
]