from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersOnlyValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PasscodeValidator:
    def __init__(self, length=6, message=None):
        self.length = length
        self.message = message or f"Your passcode must be exactly {self.length} digits!"

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Your passcode must be exactly {self.length} digits!"
        else:
            self.__message = value

    def __call__(self, value):
        if not (value.isdigit() and len(value) == self.length):
            raise ValidationError(self.message)

