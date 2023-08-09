from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Login paths
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    # Character creation
    path("create/", views.create_character, name="create_character"),
    # Character viewing
    path("character/<int:pk>/", views.character_page, name="character_page"),
    # Character updating
    path("update_character/<int:pk>/", views.update_character, name="update_character"),
    # Databsae viewing
    path("databases/", views.databases, name="databases"),
]