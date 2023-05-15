from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product/",views.product, name="product"),
    path("productapi/",views.productapi, name="productapi"),
    path("server/",views.server, name="server"),
    path("serverapi/",views.serverapi, name="serverapi"),
    path("advertise/",views.advertise, name="advertise"),
    path("advertiseapi/",views.advertiseapi, name="advertiseapi"),
]

