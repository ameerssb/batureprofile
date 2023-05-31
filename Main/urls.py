from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('research', views.Research, name="Research"),
    path('experience', views.Experience, name="Experience"),
    # path('events', views.Events, name="Events"),
    path('photos', views.Photos, name="Photos"),
    path('contact', views.Contact, name="Contact"),
]
