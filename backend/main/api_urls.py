from django.urls import path

from .medical_imaging import MedicalImagingResultView


urlpatterns = [
    # les urls de l'application home
    path('<int:hospital_id>/<int:profile_id>/<int:patient_id>/fiches/<int:fiche_id>/imaging_vouchers/<int:voucher_id>/imaging_result',
         MedicalImagingResultView.as_view(), name='api_medical_imaging_result'),
]
