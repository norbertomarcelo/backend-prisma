from django.test import TestCase
from appointment.models import Person
from appointment.validators import name_validator, cpf_validator, phone_validator


class PersonTestCase(TestCase):
    def setUp(self):
        self.validated_person = Person(
            name='Maria Joaquina',
            cpf='08888281010',
            phone_number='32 98801-5296',
            email='user@user.com',
            created_at='2023-08-20',
            updated_at='2023-08-23'
        )

    def test_create_valid_person(self):
        self.assertEqual(self.validated_person.name, 'Maria Joaquina')
        self.assertEqual(self.validated_person.cpf, '08888281010')
        self.assertEqual(self.validated_person.phone_number, '32 98801-5296')
        self.assertEqual(self.validated_person.email, 'user@user.com')
        self.assertEqual(self.validated_person.created_at, '2023-08-20')
        self.assertEqual(self.validated_person.updated_at, '2023-08-23')
        self.assertIsNone(self.validated_person.deleted_at)

    def test_validate_attributes(self):
        self.assertIsNone(name_validator(self.validated_person.name))
        self.assertIsNone(cpf_validator(self.validated_person.cpf))
        self.assertIsNone(phone_validator(self.validated_person.phone_number))
