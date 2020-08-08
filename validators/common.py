import re
from django.core.exceptions import ValidationError


def max_length_validator(value, max_length):
    if len(value) > max_length:
        raise ValidationError(message=f"value too long, must be must be no longer than {max_length} character(s)")


def min_length_validator(value, min_length):
    if len(value) < min_length:
        raise ValidationError(message=f"value too short, must be must be longer than {min_length} character(s)")


class NumberValidator(object):
    def __init__(self, min_digits=3):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not len(re.findall(r'\d', password)) >= self.min_digits:
            raise ValidationError(
                message=f"The password must contain at least {self.min_digits} digit(s), 0-9.",
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            f"Your password must contain at least {self.min_digits} digit(s), 0-9."
        )


class UppercaseValidator(object):
    def __init__(self, min_uppercase=1):
        self.min_uppercase = min_uppercase

    def validate(self, password, user=None):
        if not re.findall(r'[A-Z]', password):
            raise ValidationError(
                message=f"The password must contain at least {self.min_uppercase} uppercase letter(s), A-Z.",
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            f"Your password must contain at least {self.min_uppercase} uppercase letter(s), A-Z."
        )


class LowercaseValidator(object):
    def __init__(self, min_lowercase=1):
        self.min_lowercase = min_lowercase

    def validate(self, password, user=None):
        if not re.findall(r'[a-z]', password):
            raise ValidationError(
                message=f"The password must contain at least {self.min_lowercase} lowercase letter(s), a-z.",
                code='password_no_lower'
            )

    def get_help_text(self):
        return _(
            f"Your password must contain at least {self.min_lowercase} lowercase letter(s), a-z."
        )


class SymbolValidator(object):
    def __init__(self, min_symbol=5):
        self.min_symbol = min_symbol

    def validate(self, password, user=None):
        if not re.findall(r'[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                message=f"The password must contain at least {self.min_symbol} symbol(s): " + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?",
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            f"Your password must contain at least {self.min_symbol} symbol(s): " + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )