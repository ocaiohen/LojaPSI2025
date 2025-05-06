from django.contrib import admin

# Register your models here.
from .models import * #importa nossos models

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = "criado_em"

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    search_fields = ('Produto',)
    exclude = ('msgPromocao',)

admin.site.register(Fabricante, FabricanteAdmin) #adiciona a interface do admin no browser
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)