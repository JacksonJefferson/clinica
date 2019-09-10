from django.contrib import admin

from . models import Paciente, Medico, Medicamento

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Medicamento)
