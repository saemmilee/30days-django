from django.urls import path
from . import views

# 네임스페이스 - 별칭때문에 사용(다른 앱과 별칭이 겹칠수도 있어서)
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]

