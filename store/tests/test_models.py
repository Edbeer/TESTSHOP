from django.test import TestCase

from store.models import Category, Product, User


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        """
        :return: name of category
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):

    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        self.data1 = Product.objects.create(category_id=1,
                                            title='django beginner',
                                            slug='django-beginner',
                                            created_by_id=1,
                                            price='20.00',
                                            image='structurehtml5')

    def test_products_model_entry(self):
        """
        Test Product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginner')
