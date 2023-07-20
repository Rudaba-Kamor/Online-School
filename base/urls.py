from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('classroom/', views.classroom, name= 'classroom'),
    path('blog/', views.blog, name= 'blog'),
    path('contact/', views.contact, name= 'contact'),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('about/', views.about, name= 'about'),
]