from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blogpost, name='blog'),
    path('blog/<str:slug>', views.blog, name='blog'),
]