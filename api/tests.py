# Django imports
from django.urls import reverse

# Rest framework imports
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase

# App imports
from .models import Investor


class TestInvestorApi(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.investor = Investor(
            full_name = 'george soros'
        )
        self.investor.save()

    def test_investor_list(self):
        url = reverse('investor-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.investor.full_name in response.data[0]['full_name'])

    def test_investor_detail(self):
        url = reverse('investor-detail', args=(self.investor.id, ))
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.investor.full_name in response.data['full_name'])

    def test_investor_delete(self):
        url = reverse('investor-delete', args=(self.investor.id, ))
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals('Data deleted', response.data)
    
    def test_investor_create(self):
        data = {"full_name" : "charlie munger"}
        url = reverse('investor-create')
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue('charlie munger' in response.data['full_name'])

    def test_investor_update(self):
        data = {"full_name" : "charlie munger"}
        url = reverse('investor-update', args=(self.investor.id, ))
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue('charlie munger' in response.data['full_name'])
    