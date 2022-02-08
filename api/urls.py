from django.contrib import admin
from django.urls import path
from decrypt.api import DecryptMessageAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('decryptMessage', DecryptMessageAPI.as_view())
]
