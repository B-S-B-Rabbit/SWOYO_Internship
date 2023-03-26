from unittest import TestCase, main
from rome_numbers.roman_numerals_to_int import roman_numerals_to_int


class MyTestCase(TestCase):
    def test_one_digit(self):
        self.assertEqual(roman_numerals_to_int("I"), 1)
        self.assertEqual(roman_numerals_to_int("II"), 2)
        self.assertEqual(roman_numerals_to_int("III"), 3)
        self.assertEqual(roman_numerals_to_int("IIII"), None)
        self.assertEqual(roman_numerals_to_int("IV"), 4)
        self.assertEqual(roman_numerals_to_int("IVI"), None)
        self.assertEqual(roman_numerals_to_int("IIIV"), None)
        self.assertEqual(roman_numerals_to_int("VV"), None)
        self.assertEqual(roman_numerals_to_int("VII"), 7)
        self.assertEqual(roman_numerals_to_int("IX"), 9)

    def test_two_digits(self):
        self.assertEqual(roman_numerals_to_int("XIII"), 13)
        self.assertEqual(roman_numerals_to_int("XIV"), 14)
        self.assertEqual(roman_numerals_to_int("XVV"), None)
        self.assertEqual(roman_numerals_to_int("XXX"), 30)
        self.assertEqual(roman_numerals_to_int("XXXX"), None)
        self.assertEqual(roman_numerals_to_int("XVX"), None)
        self.assertEqual(roman_numerals_to_int("XXV"), 25)
        self.assertEqual(roman_numerals_to_int("XIX"), 19)
        self.assertEqual(roman_numerals_to_int("XVIIIII"), None)
        self.assertEqual(roman_numerals_to_int("XL"), 40)
        self.assertEqual(roman_numerals_to_int("LL"), None)
        self.assertEqual(roman_numerals_to_int("LXXXVIII"), 88)
        self.assertEqual(roman_numerals_to_int("VL"), None)
        self.assertEqual(roman_numerals_to_int("IL"), None)
        self.assertEqual(roman_numerals_to_int("XLIX"), 49)
        self.assertEqual(roman_numerals_to_int("IC"), None)
        self.assertEqual(roman_numerals_to_int("XC"), 90)
        self.assertEqual(roman_numerals_to_int("XCVIII"), 98)

    def test_three_digits(self):
        self.assertEqual(roman_numerals_to_int("CDM"), None)
        self.assertEqual(roman_numerals_to_int("CIII"), 103)
        self.assertEqual(roman_numerals_to_int("CLV"), 155)
        self.assertEqual(roman_numerals_to_int("VCL"), None)
        self.assertEqual(roman_numerals_to_int("CDC"), None)
        self.assertEqual(roman_numerals_to_int("CXX"), 120)
        self.assertEqual(roman_numerals_to_int("XXC"), None)
        self.assertEqual(roman_numerals_to_int("CVIICII"), None)
        self.assertEqual(roman_numerals_to_int("CD"), 400)
        self.assertEqual(roman_numerals_to_int("DD"), None)
        self.assertEqual(roman_numerals_to_int("DCCC"), 800)
        self.assertEqual(roman_numerals_to_int("DCCCLXXXVIII"), 888)
        self.assertEqual(roman_numerals_to_int("DXD"), None)
        self.assertEqual(roman_numerals_to_int("XM"), None)
        self.assertEqual(roman_numerals_to_int("DM"), None)
        self.assertEqual(roman_numerals_to_int("CM"), 900)

    def test_four_digits(self):
        self.assertEqual(roman_numerals_to_int("MMM"), 3000)
        self.assertEqual(roman_numerals_to_int("MMMCMXCIX"), 3999)
        self.assertEqual(roman_numerals_to_int("MMMM"), None)
        self.assertEqual(roman_numerals_to_int("MCMLX"), 1960)
        self.assertEqual(roman_numerals_to_int("MMCDVII"), 2407)
        self.assertEqual(roman_numerals_to_int("MCMXCIX"), 1999)
        self.assertEqual(roman_numerals_to_int("MXLD"), None)
        self.assertEqual(roman_numerals_to_int("MDCCC"), 1800)
        self.assertEqual(roman_numerals_to_int("MDCCCLXXXVIII"), 1888)
        self.assertEqual(roman_numerals_to_int("MDXD"), None)

    def test_wrong_values(self):
        self.assertEqual(roman_numerals_to_int(2.7), None)
        self.assertEqual(roman_numerals_to_int("4"), None)
        self.assertEqual(roman_numerals_to_int("MMMA"), None)
        self.assertEqual(roman_numerals_to_int("some_str"), None)
        self.assertEqual(roman_numerals_to_int(["XXX"]), None)
        self.assertEqual(roman_numerals_to_int(28), None)
