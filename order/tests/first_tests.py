from django.test import TestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order

# Create your tests here.
class OrderTestCase(TestCase):
    def test_create_order(self):
        self.user = UserFactory.build()
        self.user.save()

        self.order = OrderFactory.build(user=self.user)
        self.order.save()

        self.assertTrue(Order.objects.filter(user=self.user).exists())
