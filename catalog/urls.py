from django.urls import path

from catalog.views import contacts, home, product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('product/', product, name='product'),
]
