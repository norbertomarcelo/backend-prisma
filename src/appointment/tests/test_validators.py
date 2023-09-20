from django.test import TestCase
from django.core.exceptions import ValidationError
from appointment.validators import name_validator, cpf_validator, phone_validator


class ValidatorsTestCase(TestCase):

    def test_name_validator(self):
        self.assertIsNone(name_validator('Lin-Manuel Miranda'))
        self.assertIsNone(name_validator('José Aragão'))
        self.assertRaises(ValidationError, name_validator,
                          'Maria Joaquina 123')
        self.assertRaises(ValidationError, name_validator,
                          'M@ria Joaqu|na $ilv4')

    def test_cpf_validator(self):
        self.assertIsNone(cpf_validator('08888281010'))
        self.assertIsNone(cpf_validator('088.882.810-10'))
        self.assertRaises(ValidationError, cpf_validator, '08888281011')
        self.assertRaises(ValidationError, cpf_validator, '088.882.810-11')

    def test_phone_validator(self):
        self.assertIsNone(phone_validator('32 98801-5296'))
        self.assertRaises(ValidationError, phone_validator, '32988015296')
        self.assertRaises(ValidationError, phone_validator, '32 988015296')
        self.assertRaises(ValidationError, phone_validator, '32 98801-529')
        self.assertRaises(ValidationError, phone_validator, '32 9880-52966')
        self.assertRaises(ValidationError, phone_validator, '32 98801-52a6')
