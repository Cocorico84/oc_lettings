from django.test import TestCase
from django.urls.base import reverse


class OCTest(TestCase):
    def test_index(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Holiday Homes", response.content)
