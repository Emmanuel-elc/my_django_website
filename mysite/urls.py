from django.contrib import admin
from django.urls import path, include  # include is needed to include app urls

urlpatterns = [
    path('admin/', admin.site.urls),       # Django admin
    path('', include('myprofile.urls')),   # root URL routed to myprofile app
]
