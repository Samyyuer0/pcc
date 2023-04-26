from django.contrib import admin

from .models import Endereco
from .models import Pessoa
from .models import Depoimento

admin.site.register(Endereco)
admin.site.register(Pessoa)
admin.site.register(Depoimento)

# Register your models here.
