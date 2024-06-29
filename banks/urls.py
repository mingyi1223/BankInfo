from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<bank_code>/<branch_code>/<bank_title>-<branch_title>.html', views.index, name='detail'),
]