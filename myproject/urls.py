from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('', include('firstpage.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')), 
]