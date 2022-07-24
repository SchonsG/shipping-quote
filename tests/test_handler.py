import unittest

from pony.orm import db_session
from src.handler import shipping_quote
from src.models import Transporter


class TestHandler(unittest.TestCase):
    @classmethod
    @db_session
    def setUpClass(cls):
        Transporter(
            name="Entrega Ninja",
            constant=0.3,
            max_height=200,
            min_height=10,
            max_width=140,
            min_width=6,
            delivery_time=6,
        )

        Transporter(
            name="Entrega KaBuM",
            constant=0.2,
            max_height=140,
            min_height=5,
            max_width=125,
            min_width=13,
            delivery_time=4,
        )

        return super().setUpClass()

    @classmethod
    @db_session
    def tearDownClass(cls):
        Transporter.select().delete(bulk=True)

        return super().tearDownClass()

    def test_shipping_quote_all_outputs(self):
        entry = {
            "dimensao": {
                "altura": 102,
                "largura": 40,
            },
            "peso": 400,
        }

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

        result = shipping_quote(entry)

        self.assertListEqual(result["body"], expected)

    def test_shipping_quote_one_output(self):
        entry = {
            "dimensao": {
                "altura": 152,
                "largura": 50,
            },
            "peso": 850,
        }

        expected = [
            {
                "nome": "Entrega Ninja",
                "valor_frete": 25.50,
                "prazo_dias": 6,
            }
        ]

        result = shipping_quote(entry)

        self.assertListEqual(result["body"], expected)

    def test_shipping_quote_without_output(self):
        entry = {
            "dimensao": {
                "altura": 230,
                "largura": 162,
            },
            "peso": 5600,
        }

        expected = []

        result = shipping_quote(entry)

        self.assertListEqual(result["body"], expected)

    def test_shipping_quote_without_necessary_weight(self):
        entry = {
            "dimensao": {
                "altura": 140,
                "largura": 40,
            },
            "peso": 0,
        }

        expected = []

        result = shipping_quote(entry)

        self.assertListEqual(result["body"], expected)
