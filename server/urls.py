from django.urls import path
from .views import *

urlpatterns = [
    path('', Login ,  name="Login_Page" ),
    path('Data' , Data , name="DataBase"),
    path("category" , Category , name="Category_Edit"),
    path("services" , Service , name="Service_Edit"),
    path("product" , Product , name="Product_Edit")
]