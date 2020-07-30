from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task  
from datetime import datetime
# Create your views here.
@login_required(login_url='/contas/login/')
def home(request):
    template_name = 'core/home.html'
    #print('Método da requisição: ', request.method)
    #print('Path da requisição: ', request.path)
    tasks = Task.objects.filter(owner__username=request.user, end_date=datetime.today()).exclude(status='CD')
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def search_tasks(request):
    template_name = 'core/search_tasks.html'
    query = request.GET.get('query')
    tasks = Task.objects.filter(name__icontains=query, owner=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context)