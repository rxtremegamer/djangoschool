from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePage, name='home-page'),
    path('contact/', ContactPage, name='contact-page'),
    path('about/', AboutPage, name='about-page'),
    path('score/', ShowScore, name='score-page')
]
