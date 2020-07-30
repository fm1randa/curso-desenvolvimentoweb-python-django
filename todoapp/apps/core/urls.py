from django.urls import path

app_name = 'core'

from . import views

urlpatterns = [
    path('pesquisar', views.search_tasks, name='search_tasks'),
    path('', views.home, name='home'),
]