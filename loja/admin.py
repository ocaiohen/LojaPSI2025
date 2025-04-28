from django.contrib import admin

# Register your models here.
from .models import * #importa nossos models
admin.site.register(Fabricante) #adiciona a interface do admin no browser
admin.site.register(Categoria)
admin.site.register(Produto)