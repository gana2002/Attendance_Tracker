from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lc/', views.lc, name='lc'),
    path('pp/', views.pp, name='pp'),
    path('lp/', views.lp, name='lp'),
    path('login/', views.loginPage, name='login'),
]