from django.shortcuts import render

# Create your views here.

def home(request):
    print('Método da requisição: ', request.method)
    print('Path da requisição: ', request.path)
    return render(request, 'base.html', {})