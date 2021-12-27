from django.test import TestCase
from django.urls.base import reverse

from .models import Address, Letting


class LettingTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="123 rue bidon",
            city="Testville",
            state="Test",
            zip_code=11111,
            country_iso_code=123,
        )
        self.letting = Letting.objects.create(title="youpi", address=self.address)

    def test_index(self):
        url = reverse("lettings_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Lettings", response.content)
        self.assertIn(b"youpi", response.content)

    def test_letting(self):
        url = reverse("letting", kwargs={"letting_id": 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"123 rue bidon", response.content)
