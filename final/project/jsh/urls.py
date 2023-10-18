from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('about/', views.about_us, name='about_us'), 
    path('contact/', views.contact_us, name='contact_us'),
    path('login/', views.user_login, name='login'),  
    path('register/', views.registration, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
