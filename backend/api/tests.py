from http import HTTPStatus

from django.test import Client, TestCase

from api import models


class TaskiAPITestCase(TestCase):
    """Tests for Task API endpoints."""

    def setUp(self):
        """Set up test environment."""
        self.guest_client = Client()

    def test_list_exists(self):
        """Check that task list endpoint is accessible."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Check that a new task can be created."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
