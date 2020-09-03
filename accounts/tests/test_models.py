from django.test import TestCase
from django.contrib import auth
from ..models import Token
User = auth.get_user_model()

class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email="a@b.com")
        token2 = Token.objects.create(email="a@b.com")
        self.assertNotEqual(token1.uid, token2.uid)

class UserModelTest(TestCase):
    def test_user_is_valid_with_email_only(self):
        user = User(email="A@B.com")
        user.full_clean()

    def test_email_is_primary_key(self):
        user = User(email="TR@C.com")
        self.assertEqual(user.pk, 'TR@C.com')

    def test_no_problem_with_auth_login(self):
        user = User.objects.create(email='edith@example.com')
        user.backend = ''
        request = self.client.request().wsgi_request
        auth.login(request, user)
