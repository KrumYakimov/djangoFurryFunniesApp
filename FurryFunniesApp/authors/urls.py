from django.urls import path

from FurryFunniesApp.authors.views import AuthorDetailView, AuthorCreateView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name="author-create"),
    path("details/", AuthorDetailView.as_view(), name="author-details"),
    path("edit/", AuthorEditView.as_view(), name="author-edit"),
    path("delete/", AuthorDeleteView.as_view(), name="author-delete"),
]