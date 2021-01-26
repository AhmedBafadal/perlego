from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Book
from ..serializers import BookSerializer

BOOK_URL = reverse('perlego:book-list')

class PublicBooksApiTest(TestCase):
    """"Test the Books API"""
    def setUp(self):
        self.client = APIClient()
        
    def test_access_page(self):
        res = self.client.get(BOOK_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        
    def test_retrieve_books(self):
        Book.objects.create(title='Book Test', countries=['United Kingdom', 'France'])
        res = self.client.get(BOOK_URL)
        
        books = Book.objects.get(title='Book Test')
        serializer = BookSerializer(books, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
