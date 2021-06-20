from .views import get_tree_path
from django.urls import path

urlpatterns = [
    path("get_tree/", get_tree_path),
]
