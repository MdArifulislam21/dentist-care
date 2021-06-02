from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('appoinment', views.appoinment, name='appoinment'),
    path('about', views.about, name='about'),
    path('patients', views.patient, name='patient'),
    path('news', views.news, name='news'),
    path('service', views.service, name='service'),


]

