from django.urls import path
from .views import home, profile, RegisterView
from . import views


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('home/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('elements/', views.elements, name='elements'),
    path('gallery/', views.gallery, name='gallery'),
    path('news/', views.news, name='news'),
    path('staff/', views.staff, name='staff'),
    path('tabletime/', views.tabletime, name='tabletime'),
    path('skorboard/', views.skorboard, name='skorboard'),
]



