from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.
class HomeTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class AboutTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class InsulinHelpTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('insulin-help'))
        self.assertEqual(response.status_code, 200)
