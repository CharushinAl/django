from django.urls import path

from catalog.views import contacts, home, product, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('product/<int:product_id>', product_detail, name='product_detail'),
]
