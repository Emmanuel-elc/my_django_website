from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # root of the site shows home.html
    # you can add more pages here later, e.g.:
    # path('about/', views.about, name='about'),
]
