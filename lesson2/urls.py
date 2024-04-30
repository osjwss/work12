from django.contrib import admin
from django.urls import path

from work12.lesson2.views import AuthorList, AuthorPages, AuthorCreate, AuthorDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search1/list/<int:pk>', AuthorList.as_view()),
    path('search2/pages/', AuthorPages.as_view())
    path('search3/', AuthorCreate.as_view())
    path('check/submit/', AuthorDelete.as_view())
    ]