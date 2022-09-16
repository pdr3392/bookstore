from django.test import TestCase
from product.factories import ProductFactory, CategoryFactory
from product.models.category import Category
from product.models.product import Product

# Create your tests here.
class ProductTestCase(TestCase):
    def test_create_product(self):
        self.product = ProductFactory.build()
        self.product.save()

        self.assertTrue(Product.objects.filter(title=self.product.title).exists())


class CategoryTestCase(TestCase):
    def test_create_category(self):
        self.category = CategoryFactory.build()
        self.category.save()

        self.assertTrue(Category.objects.filter(title=self.category.title).exists())
