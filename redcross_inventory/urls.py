from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('donations/', include('donations_app.urls')),  
]
