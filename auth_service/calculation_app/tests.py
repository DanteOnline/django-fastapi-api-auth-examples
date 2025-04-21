from rest_framework.test import APISimpleTestCase


class TestCalculationAPI(APISimpleTestCase):

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
