from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from FurryFunniesApp.authors.models import Author
from FurryFunniesApp.posts.models import Post
from FurryFunniesApp.utils.profile_helpers import get_profile
from FurryFunniesApp.web.mixins import AuthorFormPlaceholderMixin, AuthorFormHelpTextMixin


class IndexView(TemplateView):
    template_name = "web/index.html"

    def get(self, request, *args, **kwargs):
        profile = get_profile()

        if profile is None:
            return redirect("author-create")

        return self.render_to_response({'profile_exists': profile is not None})


class DashboardView(ListView):
    model = Post
    template_name = 'web/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_exists'] = get_profile() is not None
        return context
