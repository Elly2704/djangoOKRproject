from django.contrib.auth.views import LogoutView
from django.template.defaulttags import url
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book-detail/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author-detail/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('login/', views.LoginUser.as_view, name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian')
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

]

