from django.test import TestCase

from api.models import Customer


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.customer_name = "Write world class code"
        self.customer = Customer(name=self.customer_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)

        # Add these imports at the top
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.customer_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.customer_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        customer = Customer.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': customer.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, customer)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        change_customer = {'name': 'Something new'}
        customer = Customer.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': customer.id}),
            change_customer, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        customer = Customer.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': customer.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)