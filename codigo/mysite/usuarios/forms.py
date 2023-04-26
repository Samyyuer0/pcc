from django.forms import ModelForm
from .models import Pessoa, Depoimento, Endereco

class PessoaForm(ModelForm):
    
    class Meta:
        model = Pessoa
        fields = "__all__"

class DepoimentoForm(ModelForm):
    
    class Meta:
        model = Depoimento
        fields = "__all__"

class EnderecoForm(ModelForm):

    class Meta:
        model = Endereco
        fields = "__all__"

class LoginForm(ModelForm):
    
    class Meta:
        model = Pessoa
        fields = "__all__"