from django.urls import path

from catalog.views import contacts, home

from django.views.generic import RedirectView

urlpatterns = [
    path('contacts/', contacts),
    path('', home),

    path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
]
