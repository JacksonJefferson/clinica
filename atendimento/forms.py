from django.forms import ModelForm
from . models import Paciente, Medico, Medicamento

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
    
class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'