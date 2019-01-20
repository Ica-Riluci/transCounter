from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginp, name='login'),
    path('login_check/', views.login_check, name='login_check')
]