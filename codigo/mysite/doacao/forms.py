from django.forms import ModelForm
from .models import Doacao, Peruca

class DoacaoForm(ModelForm):
    
    class Meta:
        model = Doacao
        fields = "__all__"

class PerucaForm(ModelForm):
    
    class Meta:
        model = Peruca
        fields = "__all__"