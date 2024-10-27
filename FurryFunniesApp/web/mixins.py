from django import forms

from FurryFunniesApp.authors.models import Author


class AuthorFormPlaceholderMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields["first_name"].widget = forms.TextInput(
            attrs={"placeholder": "Enter your first name..."}
        )

        form.fields["last_name"].widget = forms.TextInput(
            attrs={"placeholder": "Enter your last name..."}
        )

        form.fields["passcode"].widget = forms.PasswordInput(
            attrs={"placeholder": "Enter 6 digits..."}
        )

        form.fields["pets_number"].widget = forms.NumberInput(
            attrs={"placeholder": "Enter the number of your pets..."}
        )

        return form


class AuthorFormHelpTextMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["passcode"].help_text = "Your passcode must be a combination of 6 digits"
        return form


# # Example form class using both mixins
# class AuthorForm(AuthorFormPlaceholderMixin, AuthorFormHelpTextMixin, forms.ModelForm):
#     class Meta:
#         model = Author  # Replace with your actual Author model
#         fields = ['first_name', 'last_name', 'passcode', 'pets_number']
