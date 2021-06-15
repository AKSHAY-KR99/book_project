"""Book_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import mainpage,AuthorCreate,AuthorDelete,AuthorEdit,BookCreateView,ViewAllBooks,\
    DeleteBook,EditBook,SearchBook,ViewDetails,BookOrder

urlpatterns = [
    path('',mainpage),
    path('author',AuthorCreate.as_view(),name="author"),
    path('author/delete/<int:id>',AuthorDelete.as_view(),name='authordelete'),
    path('author/edit/<int:id>',AuthorEdit.as_view(),name='authoredit'),
    path('createbook',BookCreateView.as_view(),name='bookcreate'),
    path('allbooks',ViewAllBooks.as_view(),name='viewall'),
    path('delete/<int:id>',DeleteBook.as_view(),name='boodelete'),
    path('edit/<int:id>',EditBook.as_view(),name="editbook"),
    path('book/<int:id>',BookOrder.as_view(),name="book"),
    path('search',SearchBook.as_view(),name='search'),
    path('view/<int:id>',ViewDetails.as_view(),name='view')
]
