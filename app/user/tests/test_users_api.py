from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL=reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    "test user api public"

    def setUp(self):
        self.client=APIClient()

    def test_create_valid_user_success(self):
        "test creating user with valid payload is successful"
        payload={
            'email':'test@gmail.com',
            'password':'testpass',
            'name':'Test name'
        }
        res=self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user=get_user_model().objects.get(**res.data)
        self.assertTrue('password',res.data)