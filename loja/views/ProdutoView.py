from django.http import HttpResponse

def list_produto_view(request, id=None):
    if id is None:
        return HttpResponse('<h1>Lista de produtos!</h1>')
    
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)