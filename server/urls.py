from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Login ,  name="Login_Page" ),
    path('data' , Data , name="DataBase"),
    path("category" , Category , name="Category_Edit"),
    path("services" , Service , name="Service_Edit"),
    path("product" , Product , name="Product_Edit")
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)