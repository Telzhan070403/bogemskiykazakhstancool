from django.test import TestCase
from ..models import *
from random import randint


class UnitTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: Hello,admin')
        pass

    def setUp(self):
        print('setUp: Test method')
        pass

    def test_is_false(self):
        print('Method: isFalse complied')
        self.assertFalse(False)

    def test_is_add(self):
        def my():
            x = 12
            return x
        print('Method: is_add_method compiled')
        self.assertEqual(6 + 6, my())

    def test_is_multiple(self):
        def generator():
            return randint(34, 38)
            print('Method: is_multiple_method compiled')
        self.assertEqual(6 * 6, generator())
