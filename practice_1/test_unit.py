import unittest
from function import get_circle_length


class TestQuadFunc(unittest.TestCase):

    def test_1(self):
        res = get_circle_length(100, 10)
        self.assertEqual(res, 10)

    def test_2(self):
        res = get_circle_length(50, 5)
        self.assertEqual(res, 10)

    def test_3(self):
        res = get_circle_length(67, 3)
        self.assertEqual(res, 4)

    def test_4(self):
        with self.assertRaises(TypeError):
            res = get_circle_length(1)

    def test_5(self):
        with self.assertRaises(TypeError):
            res = get_circle_length(1, 2, 3)
