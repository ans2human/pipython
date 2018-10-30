from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', BlogListView.as_view() , name='blog'),
    path('blog/<str:slug>/', BlogDetailView.as_view() , name='blog'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('addproject/', views.project, name='project'),
    path('prj/', views.prj, name='prj')
]