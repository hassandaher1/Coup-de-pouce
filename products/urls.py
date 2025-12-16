from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # Interface publique
    path("", views.public_home, name="public_home"),

    # Auth et interface admin personnalisée
    path("admin/login/", auth_views.LoginView.as_view(
        template_name="admin/login.html",
        redirect_authenticated_user=True,
    ), name="admin_login"),
    path("admin/logout/", auth_views.LogoutView.as_view(), name="admin_logout"),
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    path("admin/delete/<int:product_id>/", views.admin_delete_product, name="admin_delete_product"),
]

