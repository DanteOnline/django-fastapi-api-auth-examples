from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient


class TestCalculationAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user('user', 'user@user.com', 'user123')
        self.client.force_authenticate(user)
        self.guest = APIClient()

    def test_no_auth_calculate(self):
        """
        Test /api/calculate: success 401 - no auth
        :return:
        """
        url = '/api/calculate/'
        response = self.guest.post(
            url,
            data={
                'expression': '((1+2)*3)'
            }
        )
        self.assertEqual(401, response.status_code)

    def test_calculate(self):
        """
        Test /api/calculate: success
        """
        url = '/api/calculate/'
        response = self.client.post(
            url,
            data={
                'expression': '((1+2)*3)'
            }
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual({
            'result': 9
        }, response.json())


    def test_random_expression_status_code(self):
        """
        Test /api/random-expression: success
        """
        url = '/api/random-expression/'
        response = self.client.get(
            url
        )
        self.assertEqual(200, response.status_code)
        self.assertIn('expression', response.json())


    def test_no_auth_random_expression_status_code(self):
        """
        Test /api/random-expression: success 401 - no auth
        :return:
        """
        url = '/api/random-expression/'
        response = self.guest.get(
            url
        )
        self.assertEqual(401, response.status_code)
