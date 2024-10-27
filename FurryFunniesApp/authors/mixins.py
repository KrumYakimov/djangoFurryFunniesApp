from django import forms


class AuthorFormPlaceholderMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if "first_name" in form.fields:
            form.fields["first_name"].widget = forms.TextInput(
                attrs={"placeholder": "Enter your first name..."}
            )

        if "last_name" in form.fields:
            form.fields["last_name"].widget = forms.TextInput(
                attrs={"placeholder": "Enter your last name..."}
            )

        if "passcode" in form.fields:  # Check if the passcode field exists
            form.fields["passcode"].widget = forms.PasswordInput(
                attrs={"placeholder": "Enter 6 digits..."}
            )

        if "pets_number" in form.fields:
            form.fields["pets_number"].widget = forms.NumberInput(
                attrs={"placeholder": "Enter the number of your pets..."}
            )

        return form


class AuthorFormHelpTextMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if "passcode" in form.fields:  # Check if the passcode field exists
            form.fields["passcode"].help_text = "Your passcode must be a combination of 6 digits"

        return form
