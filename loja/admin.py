from django.contrib import admin

# Register your models here.
from .models import * #importa nossos models

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = "criado_em"

admin.site.register(Fabricante, FabricanteAdmin) #adiciona a interface do admin no browser
admin.site.register(Categoria)
admin.site.register(Produto)