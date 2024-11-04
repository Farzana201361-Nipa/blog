from django.urls import path
from . import views



urlpatterns = [
    path('home/',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path("<int:id>/",views.post, name='post'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),
    path('blog_post/',views.blog_post_list, name='blog_post'),
    
]
