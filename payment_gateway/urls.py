from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home' ),
    path('base/',base,name='base' ),
    path('payment/',payment,name='payment_successful' ),
    path('list/',DonerList,name='list' ),


]
