from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('all-news/', views.All_News, name="All-News"),
    path('news/<str:urls>/', views.News, name="News"),
    path('departments/', views.Department, name="Departments"),
    path('department/<str:urls>/', views.DepartmentDetail, name="Detail"),
    path('contact-us', views.Contact, name="Contact"),
    path('about-us', views.About, name="About"),        
]
