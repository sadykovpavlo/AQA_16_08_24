import unittest
from homework_functions_file import list_numbers_calculation, count_product_price, count_total_price, \
    required_album_pages


class TestCounters(unittest.TestCase):
    # case all items is int
    def test_list_number_calculation_positive_int_only(self):
        entering_list = ['1,2,3,4', '1,2,3,4,50', '1,2,3']
        result = list_numbers_calculation(entering_list)
        expected = [10, 60, 6]
        self.assertEqual(result, expected, msg="Assert failed during testing list_number_calculation_positive no str")

    # case all items mixed type
    def test_list_number_calculation_positive_int_with_string(self):
        entering_list = ['1,2,3,4', '1,2,3,4,50', 'qwa1,2,3']
        result = list_numbers_calculation(entering_list)
        expected = [10, 60, "I can't do it, invalid literal for int() with base 10: 'qwa1'"]
        self.assertEqual(result, expected, msg="Assert failed during testing list_number_calculation_positive "
                                               "int with str")

    # case all items is string
    def test_list_number_calculation_positive_only_string(self):
        entering_list = ['q,wa', 'q,wa', 'q,wa']
        result = list_numbers_calculation(entering_list)
        expected = ["I can't do it, invalid literal for int() with base 10: 'q'",
                    "I can't do it, invalid literal for int() with base 10: 'q'",
                    "I can't do it, invalid literal for int() with base 10: 'q'"]
        self.assertEqual(result, expected, msg="Assert failed during testing list_number_calculation_positive "
                                               "only str")

    # case input unexpected type string
    def test_list_number_calculation_negative_incorrect_type(self):
        entering = 1
        with self.assertRaises(TypeError):
            result = list_numbers_calculation(entering)

    # case calculate price for two items
    def test_count_product_price_two_position_positive(self):
        list_prices = [('cake', 2, 33), ('juice', 3, 10)]
        result = count_product_price(list_prices)
        expected = 96
        self.assertEqual(result, expected, msg='Assert failed during testing count_product_price two position')

    # case calculate price for one
    def test_count_product_price_one_position_positive(self):
        list_prices = [('cake', 2, 33)]
        result = count_product_price(list_prices)
        expected = 66
        self.assertEqual(result, expected, msg='Assert failed during testing count_product_price one position')

    # case if price is negative num expected no errors
    def test_count_product_price_one_position_positive_negative_number(self):
        # Here -33 at tuple
        list_prices = [('cake', 2, -33)]
        result = count_product_price(list_prices)
        expected = -66
        self.assertEqual(result, expected, msg='Assert failed during testing count_product_price one position'
                                                'negative_number')

    # function from homework 7 to calculate full price of item with partial payment simple case
    def test_count_total_price_positive(self):
        entering_numbers = (2, 18)
        result = count_total_price(*entering_numbers)
        expected = 36
        self.assertEqual(result, expected, msg="Assert failed during testing count_total_price positive num entered")

    # case if payment is negative num expected no errors
    def test_count_total_price_negative_numb(self):
        entering_numbers = (-2, 18)
        result = count_total_price(*entering_numbers)
        expected = -36
        self.assertEqual(result, expected, msg="Assert failed during testing count_total_price negative num entered")

    # check how many page required for photo function is division
    def test_required_album_pages_positive(self):
        entering_numbers = (18, 2)
        result = required_album_pages(*entering_numbers)
        expected = 9
        self.assertEqual(result, expected, msg='Assert failed during testing required_album_page positive')

    def test_required_album_pages_division_less_to_big(self):
        entering_numbers = (2, 18)
        result = required_album_pages(*entering_numbers)
        expected = 0.1111111111111111
        self.assertEqual(result, expected, msg='Assert failed during testing required_album_page positive')

    # test case we have 0 album page
    def test_required_album_pagesZeroDivision(self):
        entering_numbers = (10, 0)
        with self.assertRaises(ZeroDivisionError):
            result = required_album_pages(*entering_numbers)


if __name__ == '__main__':
    unittest.main()
