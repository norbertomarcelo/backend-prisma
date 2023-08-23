import re
from validate_docbr import CPF
from django.core.exceptions import ValidationError


def name_validator(value):
    if re.findall(r'[^A-Za-z]', value):
        raise ValidationError(
            ('This name has invalid characters.'),
            params={"value": value},
        )

def cpf_validator(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(
            ('Invalid CPF number.'),
            params={"value": value},
        )


def phone_validator(value):
    template = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    if not re.findall(template, value):
        raise ValidationError(
            ('Invalid phone number.'),
            params={"value": value},
        )
