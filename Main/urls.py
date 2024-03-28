from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('hint', views.Hints, name="Hint"),
    path('research', views.Researchs, name="Research"),
    path('experience', views.Experiences, name="Experience"),
    path('project', views.Cat_Project, name="Cat_Project"),
    path('project/<str:cat_name>/', views.Projects, name="Project"),
    path('project/<str:cat_name>/<int:pk>/', views.ProjectPage, name="ProjectPage"),    
    path('photos', views.Photoss, name="Photos"),
    path('contact', views.Contacts, name="Contact"),
]
