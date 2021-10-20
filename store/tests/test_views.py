from unittest import skip

from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from store.models import Product, Category
from store.views import product_all


@skip('demostration skip')
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponse(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        self.data1 = Product.objects.create(category_id=1,
                                            title='django beginner',
                                            slug='django-beginner',
                                            created_by_id=1,
                                            price='20.00',
                                            image='structurehtml5')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        :return:
        """
        response = self.c.get('/', HTTP_HOST='noadress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginner']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test category response status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        request = HttpRequest()
        response = product_all(request)
        html = response.content.decode('utf-8')
        print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/django-beginner')
        response = product_all(request)
        self.assertEqual(response.status_code, 200)