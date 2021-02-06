from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("post/<int:id>", views.post, name="post"),
    path("post/add", views.addPost, name="add-post"),
    path("post/edit/<int:id>", views.editPost, name="edit-post"),
    path("post/delete/<int:id>", views.deletePost, name="delete-post"),
]