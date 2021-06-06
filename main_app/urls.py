from django.urls import path
from . import views

urlpatterns = [
    path('login_page/', views.login_page, name='login_page'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('', views.halaman_utama, name='halaman_utama')
]
