from django import forms

from FurryFunniesApp.authors.models import Author


class PostFormPlaceholderMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields["title"].widget = forms.TextInput(
            attrs={"placeholder": "Put an attractive and unique title..." }
        )

        form.fields["content"].widget = forms.Textarea(
            attrs={"placeholder": "Share some interesting facts about your adorable pets..."}
        )

        return form


class PostFormHelpTextMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["image_url"].help_text = "Share your funniest furry photo URL!"
        return form

