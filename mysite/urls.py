from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('contacts/', include('contacts.urls')),
    path('lekarstva/', include('lekarstva.urls')),
]
