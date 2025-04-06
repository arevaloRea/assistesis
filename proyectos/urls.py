from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("solicitar_cotizacion", views.request_quote, name="request_quote"),
    path("services", views.services, name="services")
]
