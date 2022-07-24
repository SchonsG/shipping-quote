import json
import unittest

from src.handler import app

app.testing = True


class TestHandler(unittest.TestCase):
    def test_shipping_quote_multiple_outputs(self):
        data = json.dumps(
            {
                "dimensao": {
                    "altura": 102,
                    "largura": 40,
                },
                "peso": 400,
            }
        )

        expected = [
            {
                "nome": "Entrega Ninja",
                "valor_frete": 12.00,
                "prazo_dias": 6,
            },
            {
                "nome": "Entrega KaBuM",
                "valor_frete": 8.00,
                "prazo_dias": 4,
            },
        ]

        with app.test_client() as client:
            response = client.post(
                "/shipping-quote", data=data, content_type="application/json"
            )

        data_response = json.loads(response.data)

        self.assertListEqual(data_response["data"], expected)

    def test_shipping_quote_one_output(self):
        data = json.dumps(
            {
                "dimensao": {
                    "altura": 152,
                    "largura": 50,
                },
                "peso": 850,
            }
        )

        expected = [
            {
                "nome": "Entrega Ninja",
                "valor_frete": 25.50,
                "prazo_dias": 6,
            }
        ]

        with app.test_client() as client:
            response = client.post(
                "/shipping-quote", data=data, content_type="application/json"
            )

        data_response = json.loads(response.data)

        self.assertListEqual(data_response["data"], expected)

    def test_shipping_quote_without_output(self):
        data = json.dumps(
            {
                "dimensao": {
                    "altura": 230,
                    "largura": 162,
                },
                "peso": 5600,
            }
        )

        expected = []

        with app.test_client() as client:
            response = client.post(
                "/shipping-quote", data=data, content_type="application/json"
            )

        data_response = json.loads(response.data)

        self.assertListEqual(data_response["data"], expected)

    def test_shipping_quote_without_necessary_weight(self):
        data = json.dumps(
            {
                "dimensao": {
                    "altura": 140,
                    "largura": 40,
                },
                "peso": 0,
            }
        )

        expected = []

        with app.test_client() as client:
            response = client.post(
                "/shipping-quote", data=data, content_type="application/json"
            )

        data_response = json.loads(response.data)

        self.assertListEqual(data_response["data"], expected)
