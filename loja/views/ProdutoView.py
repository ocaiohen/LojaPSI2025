from django.http import HttpResponse
from loja.models import Produto

from datetime import timedelta, datetime
from django.utils import timezone

def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")

    produtos = Produto.objects.all()
    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if produto is not None:
        produtos.filter(Produto__contains=produto)
    if destaque is not None:
        produtos.filter(destaque=destaque)
    if promocao is not None:
        produtos.filter(promocao=promocao)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos.filter(id=id)

    print(produtos)
    
    html = "<h1> Produtos <h1> <ul>"
    for p in produtos.all():
        html += f"<li>{p.Produto}</li>"
    html += "<ul>" 

    return HttpResponse(html)