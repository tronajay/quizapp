from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('quizie.urls')),
    path('',include('account.urls')),
]