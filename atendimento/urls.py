from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('paciente/', views.paciente_list),
    path('paciente/<int:paciente_id>', views.paciente_show),
    path('paciente/create/', views.paciente_form),
    path('medico/', views.medico_list),
    path('medico/<int:medico_id>', views.medico_show),
    path('medico/create/', views.medico_form),
    path('agendamento/', views.agendamento_list),
    path('medicamento/', views.medicamento_list),
    path('medicamento/<int:medicamento_id>', views.medicamento_show),
    path('medicamento/create/', views.medicamento_form),
    
]