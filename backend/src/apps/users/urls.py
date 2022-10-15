from django.urls import path
from apps.users.views import RegisterCaregiverAPIView, RegisterBeneficiaryAPIView

api_url_patterns = [
    path('register-caregiver/', RegisterCaregiverAPIView.as_view(), name='register_caregiver'),
    path('register-beneficiary/', RegisterBeneficiaryAPIView.as_view(), name='register_beneficiary'),
]