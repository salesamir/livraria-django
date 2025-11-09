from django.http import HttpResponse

# Create your views here.
def teste(request):
    return HttpResponse("Olá, Mundo! Esta é a minha primeira view no Django.")

def teste2(request):
    return HttpResponse("la ele")