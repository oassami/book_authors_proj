from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('book/<int:book_id>', views.view_book),
    path('author/<int:author_id>', views.view_author),
    path('add_auth_book/<int:book_id>', views.add_auth_book),
    path('authors', views.authors),
    path('author/<int:author_id>', views.view_author),
    path('add_book_auth/<int:author_id>', views.add_book_auth),
]
