import unittest

from src.handler import shipping_quote


class TestHandler(unittest.TestCase):
    def test_shipping_quote_all_outputs(self):
        entry = {
            "dimensao": {
                    "altura": 102,
                    "largura": 40
                },
            "peso": 400
        }

        expected = [
            {
                "nome": "Entrega Ninja",
                "valor_frete": 12.00,
                "prazo_dias": 6
            },
            {
                "nome": "Entrega KaBuM",
                "valor_frete": 8.00,
                "prazo_dias": 4
            }
        ]

        result = shipping_quote(entry)

        self.assertListEqual(result, expected)

    def test_shipping_quote_one_output(self):
        entry = {
            "dimensao": {
                    "altura": 152,
                    "largura": 50,
                },
            "peso": 850
        }

        expected = [
            {
                "nome": "Entrega Ninja",
                "valor_frete": 25.50,
                "prazo_dias": 6
            }
        ]

        result = shipping_quote(entry)

        self.assertListEqual(result, expected)

    def test_shipping_quote_without_output(self):
        entry = {
            "dimensao": {
                    "altura": 230,
                    "largura": 162,
                },
            "peso": 5600
        }

        expected = []

        result = shipping_quote(entry)

        self.assertListEqual(result, expected)
