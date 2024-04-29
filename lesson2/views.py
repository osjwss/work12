from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book,Author
from django.views.generic.detail import PagesList
# Create your views here.

class AuthorListView(ListView):
    model = Author
    templates_name: str = "lesson2/author_list.html"
    contentx_object_name = "author"


class AuthorPages(PagesList):
    model = Author
    contentx_object_name = "author"


class AuthorCreate(CreateList):
    model = author
    fields = "__all__"
    success 