from django.urls import path
from.views import add_to_cart,cart_view,cart_delete,update_cart


urlpatterns=[
    path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart'),
    path('cart/',cart_view, name='cart'),
    path('cart_delete/<int:id>/',cart_delete,name='cart_delete'),
    path('updatecart/<int:id>/',update_cart, name="updatecart")

    

]