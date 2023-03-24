from unittest import TestCase, main
from prime_n.prime_numbers import prime_numbers


class MyTestCase(TestCase):
    def test_high_less_low(self):
        self.assertListEqual(prime_numbers(1, 0), [])

    def test_negative_values(self):
        self.assertListEqual(prime_numbers(-1, 10), [])

    def test_zero_range(self):
        self.assertListEqual(prime_numbers(100, 100), [])

    def test_full_range_small_even(self):
        self.assertListEqual(prime_numbers(0, 100),
                             [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                              89, 97])

    def test_full_range_small_odd(self):
        self.assertListEqual(prime_numbers(1, 99),
                             [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                              89, 97])

    def test_full_range_big_success(self):
        self.assertTrue(prime_numbers(1, 10 ** 6))

    def test_cut_range_small(self):
        self.assertListEqual(prime_numbers(40, 120),
                             [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113])

    def test_cut_range_small_success(self):
        self.assertTrue(prime_numbers(10 ** 3, 10 ** 6))

    def test_continue(self):
        self.assertListEqual(prime_numbers(122, 139),
                             [127, 131, 137, 139])

    def test_small_big_range(self):
        self.assertListEqual(prime_numbers(14349454, 14349484), [14349463, 14349469, 14349473])


if __name__ == '__main__':
    main()
