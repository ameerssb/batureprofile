from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('research', views.Researchs, name="Research"),
    path('experience', views.Experiences, name="Experience"),
    path('project', views.Projects, name="Project"),
    path('photos', views.Photoss, name="Photos"),
    path('contact', views.Contacts, name="Contact"),
]
