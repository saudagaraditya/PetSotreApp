from django.urls import path
from .import views
urlpatterns = [
    path('pets-list/',views.pets_list,name='pets-list'),
    path('dog_list/',views.dog_list,name='dog_list'),
    path('cat_list',views.cat_list,name='cat_list'),
    path('pet-detail/<int:pk>',views.pet_detail,name='pet-detail'),
    path('search/',views.search,name='search'),
]