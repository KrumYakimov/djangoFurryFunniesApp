from django.urls import path, include

from FurryFunniesApp.posts.views import PostCreateView, PostDetailView, PostEditView, PostDeleteView

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>", include([
        path("details/", PostDetailView.as_view(), name="post-details"),
        path("etit/", PostEditView.as_view(), name="post-edit"),
        path("delete/", PostDeleteView.as_view(), name="post-delete")
    ])),
]
