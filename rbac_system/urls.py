from django.contrib import admin
from django.urls import path
from rbac_app import views  # Import the views from the new app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add the home view for the root URL
]
