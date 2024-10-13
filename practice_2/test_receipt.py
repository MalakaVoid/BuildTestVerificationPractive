import unittest
from main import Recipe


class TestRecipe(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.portion_error = "Порции должны быть положительным целым числом!"
        self.raw_error = "Атрибут raw должен быть булевым значением!"
        self.portions_amount = 3
        self.wrong_portion = -1
        self.wrong_raw = 'string'

    @classmethod
    def setUp(self):
        receipt = {
            "name": "Долма",
            "ingredients": [
                ('Говядина', 100, 83, 1, 150),
                ('Свинной фарш', 50, 43, 2, 80),
                ('Репчатый лук', 80, 60, 1, 40),
                ('Листья винограда', 25, 21, 4, 20),
                ('Круглый рис', 100, 80, 1, 40),
                ('Сыр', 80, 60, 1, 120)
            ]
        }
        self.receipt = Recipe(receipt)

    def test_calc_cost(self):
        self.assertEqual(self.receipt.calc_cost(), 590)

    def test_calc_cost_with_portions(self):
        self.assertEqual(self.receipt.calc_cost(portions=self.portions_amount), 1770)

    def test__calc_cost_wrong_portions(self):
        with self.assertRaises(ValueError) as error:
            self.receipt.calc_cost(portions=-1)
        self.assertEqual(str(error.exception.args[0]), self.portion_error)

    def test_calc_weight_raw(self):
        self.assertEqual(self.receipt.calc_weight(raw=True), 560)

    def test_calc_weight_raw_with_portions(self):
        self.assertEqual(self.receipt.calc_weight(portions=self.portions_amount, raw=True), 1680)

    def test_calc_weight_cooked(self):
        self.assertEqual(self.receipt.calc_weight(raw=False), 453)

    def test_calc_weight_cooked_with_portions(self):
        self.assertEqual(self.receipt.calc_weight(portions=self.portions_amount, raw=False), 1359)

    def test_calc_weight_wrong_portions(self):
        with self.assertRaises(ValueError) as error:
            self.receipt.calc_weight(portions=self.wrong_portion)
        self.assertEqual(str(error.exception.args[0]), self.portion_error)

    def test_calc_weight_wrong_raw(self):
        with self.assertRaises(ValueError) as error:
            self.receipt.calc_weight(raw=self.wrong_raw)
        self.assertEqual(str(error.exception.args[0]), self.raw_error)

    def test_get_name(self):
        self.assertEqual(str(self.receipt), "Долма")

    @classmethod
    def tearDownClass(self):
        del self.receipt


if __name__ == '__main__':
    unittest.main()

