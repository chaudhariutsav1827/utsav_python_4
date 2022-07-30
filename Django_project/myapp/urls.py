from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('sign up/',views.signup,name='sign up'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
]
