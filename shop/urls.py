from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
path('category/', views.category_list, name='category_list'),
path('category/new', views.category_new, name='category_new'),
path('category/update/<slug:slug>/', views.category_update, name='category_update'),

path('product/', views.product_list, name='product_list'),
path('product/<slug:category_slug>/', views.product_list,name='product_list_by_category'),
path('product/new', views.product_new, name='product_new'),
# path('product/<slug:slug>/', views.product_detail, name='product_detail'),
path('product/update/<slug:slug>/', views.product_update, name='product_update'),
]