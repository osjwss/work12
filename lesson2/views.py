from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book,Author
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
# Create your views here.

class AuthorList(ListView):
    model = Author
    templates_name: str = "lesson2/author_list.html"
    contentx_object_name = "author"


class AuthorPages(DetailView):
    model = Author
    context_object_name = "author"


class AuthorCreate(CreateView):
    model = Author
    fields = "__all__"
    template_name: str = "lesson2/author_create.html"
    success_url = reverse_lazy('login')


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('login')
    template_name =  "lesson2/author_create.html"