from django.urls import path
from patients.views import patient_list, patient_detail, patient_create, patient_edit, patient_delete

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('<int:pk>/', patient_detail, name='patient_detail'),
    path('create/', patient_create, name='patient_create'),
    path('<int:pk>/edit/', patient_edit, name='patient_edit'),
    path('<int:pk>/delete/', patient_delete, name='patient_delete'),
]