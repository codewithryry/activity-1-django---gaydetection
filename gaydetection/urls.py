from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('detection/', include('detection.urls')),
    path('analysis/', include('analysis.urls')),
    path('detect/', include('detection.urls')), 
]