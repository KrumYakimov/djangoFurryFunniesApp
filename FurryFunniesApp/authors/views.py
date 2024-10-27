from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from FurryFunniesApp.authors.mixins import AuthorFormPlaceholderMixin, AuthorFormHelpTextMixin
from FurryFunniesApp.authors.models import Author
from FurryFunniesApp.utils.profile_helpers import get_profile


class AuthorCreateView(AuthorFormPlaceholderMixin, AuthorFormHelpTextMixin, CreateView):
    model = Author
    fields = ["first_name", "last_name", "passcode", "pets_number"]
    template_name = "authors/create-author.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = "authors/details-author.html"
    context_object_name = "author"

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        posts = author.posts.all()
        context['post_count'] = posts.count()
        context['last_post'] = posts.latest('updated_at') if posts.exists() else None
        return context


class AuthorEditView(AuthorFormPlaceholderMixin, AuthorFormHelpTextMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_profile()

    def get_success_url(self):
        return reverse_lazy('author-details')


class AuthorDeleteView(DeleteView):
    template_name = "authors/delete-author.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
