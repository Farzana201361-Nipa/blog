from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path("<int:id>/",views.post, name='post'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact')
]
