from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Django_admin/', admin.site.urls),
    path('admin/' , include("server.urls")),
    path('' ,  include("client.urls")),
    
]
