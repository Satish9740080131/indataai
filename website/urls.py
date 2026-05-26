from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('event/', views.event, name='event'),
    path('client/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('request-quote/', views.request_quote, name='request_quote'),
]
