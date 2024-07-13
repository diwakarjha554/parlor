from django.urls import path
from client.views import *

urlpatterns = [
    path('', index , name="Home"),
    path('about' , About_Us , name="About"),
    path('cart' , Cart , name="About"),
    path('categories' , Categories , name="About"),
    path('checkout' , Check_Out , name="About"),
    path('clientlogin' , Client_Login , name="About"),
    path('contact' , Contact , name="About"),
    path('item' , Items , name="About"),
    path('review' , Review , name="About"),
    path('service' , Service , name="About"),
    path('shop' , Shop , name="About"),
    path('thankyou' , Confirm , name="About"),
    
]
