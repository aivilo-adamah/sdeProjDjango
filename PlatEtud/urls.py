from . import views
from django.urls import path

urlpatterns =[
    path('', views.AcceuilView, name='Acceuil'),
    path('login/', views.LoginView, name='login'),
    path('registration/', views.RegistrationView, name='registration'),
    path('Cour/', views.CoursView, name='cour'),
    path('contact/', views.ContactView, name='contact'),
    path('search/', views.SearchView, name='search'),
    # path('py/', views.Search_pythonView, name='python'),


]