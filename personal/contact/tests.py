from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm
from .models import ContactMessage

class ContactTests(TestCase):

    def setUp(self):
        # Initialize test client
        self.client = Client()
        self.contact_url = reverse('contact')

    def test_contact_page_response(self):
        """Test that the contact page loads correctly (HTTP 200)."""
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)

    def test_contact_form_save(self):
        """Test that submitting a valid contact form saves data to the database."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Hello, this is a test message.',
            'nickname': ''  # honeypot field
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        contact_instance = form.save()
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(contact_instance.name, 'Test User')
        self.assertEqual(contact_instance.email, 'test@example.com')
