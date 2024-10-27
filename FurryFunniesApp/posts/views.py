from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from FurryFunniesApp.posts.mixins import PostFormPlaceholderMixin, PostFormHelpTextMixin
from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.utils.mixins import ReadOnlyFormMixin
from FurryFunniesApp.utils.profile_helpers import get_profile


class PostCreateView(PostFormPlaceholderMixin, PostFormHelpTextMixin, CreateView):
    model = Post
    fields = ["title", "image_url", "content"]
    template_name = "posts/create-post.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.author = profile
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/details-post.html"
    context_object_name = "post"


class PostEditView(PostFormPlaceholderMixin, PostFormHelpTextMixin, UpdateView):
    model = Post
    template_name = "posts/edit-post.html"
    fields = ["title", "image_url", "content"]
    success_url = reverse_lazy('dashboard')


class PostDeleteView(PostFormHelpTextMixin, ReadOnlyFormMixin, DeleteView):
    model = Post
    template_name = "posts/delete-post.html"
    form_class = modelform_factory(
        Post,
        fields=(
            ["title", "image_url", "content"]
        )
    )
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

