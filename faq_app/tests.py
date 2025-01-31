from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")

