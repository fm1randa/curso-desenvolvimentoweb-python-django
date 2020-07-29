from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/contas/login/')
def home(request):
    #print('Método da requisição: ', request.method)
    #print('Path da requisição: ', request.path)
    return render(request, 'base.html', {})