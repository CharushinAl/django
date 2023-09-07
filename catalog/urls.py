from django.urls import path

from catalog.views import contacts, home, product


urlpatterns = [
    path('contacts/', contacts),
    path('', home),
    path('product/', product),

]
