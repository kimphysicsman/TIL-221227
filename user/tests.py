from django.urls import reverse

from rest_framework.test import APITestCase

from user.models import User as UserModel

class UserViewTest(APITestCase):
    def setUp(self):
        user_data = {
            "username": "kimphysicsman",
            "password": "4885"
        }

        UserModel.objects.create_user(**user_data)
    
    def test_sign_in_user(self):
        sing_in_data = {
            "username": "kimphysicsman",
            "password": "4885"
        }

        response = self.client.post(
            reverse("user"),
            sing_in_data,
            format="json"
        )

        print(response.data)