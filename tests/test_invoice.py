import unittest
from dsc.invoice import InvoiceHTMLParser
import os


TEST_FOLDER = os.path.join(os.path.dirname(__file__))


class TestInvoiceHTMLParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        input = os.path.join(TEST_FOLDER, 'invoice_data.html')
        with open(input, 'r') as f:
            cls.html = f.read()

    def setUp(self):
        self.parser = InvoiceHTMLParser()
        self.parser.feed(self.html)

    def test_order_id(self):
        self.assertEqual(self.parser.get_order_id(), '890348')

    def test_shipping_email(self):
        self.assertEqual(
            self.parser.shipping_email(),
            'david.knecht@uconn.edu')

    def test_consumer_email(self):
        self.assertEqual(
            self.parser.consumer_email(),
            'abc@abc.edu')