
from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    path('', views.index, name='index'),
    path('before', views.before, name='before'),
    path('after', views.after, name='after'),
]