from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',CategoryListCreateView.as_view(),name="category_add_list"),

    # retrive single data, update, delete
    path('categories/<int:pk>/',CategoryRetriveDeleteUpdateView.as_view(),name='product_retrive_update_delete'),

    path('products/',ProductListCreateView.as_view(),name="category_add_list"),

    # retrive single data, update, delete
    path('products/<int:pk>/',ProductRetriveDeleteUpdateView.as_view(),name='product_retrive_update_delete')
]