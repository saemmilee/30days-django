
from django.urls import path
from . import views

# 네임스페이스 - 별칭때문에 사용(다른 앱과 별칭이 겹칠수도 있어서)
app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]