from django.test import TestCase
from django.urls.base import reverse

from .models import Profile, User


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_index(self):
        url = reverse("profiles_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Profiles", response.content)

    def test_profile(self):
        url = reverse("profile", kwargs={"username": "test"})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"test", response.content)
