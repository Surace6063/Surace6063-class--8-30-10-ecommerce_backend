from django.urls import path
from .views import *

urlpatterns = [
    # category
    path('categories/',CategoryListCreateView.as_view(),name="category_add_list"),
    path('categories/<int:pk>/',CategoryRetriveDeleteUpdateView.as_view(),name='product_retrive_update_delete'),
    
    # product
    path('products/',ProductListCreateView.as_view(),name="category_add_list"),
    path('products/<int:pk>/',ProductRetriveDeleteUpdateView.as_view(),name='product_retrive_update_delete'),

    #order
    path('order/create/',OrderCreateView.as_view(),name="order_create")
]