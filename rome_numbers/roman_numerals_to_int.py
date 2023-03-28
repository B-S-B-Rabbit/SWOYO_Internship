"""
Модуль roman_numerals_to_int содержит функцию, реализующую перевод чисел из римской нотации в целочисленную десятичную.
"""
__author__ = 'Андрей Помошников'


from re import match
from typing import TypeVar

int_or_none = TypeVar('int_or_none', int, None)


def roman_numerals_to_int(roman_numeral: str) -> int_or_none:
    if not isinstance(roman_numeral, str):
        return None

    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not match(r"^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$", roman_numeral):
        return None

    result = 0
    prev_val = 0

    for c in reversed(roman_numeral):
        curr_val = roman_to_int[c]

        if curr_val >= prev_val:
            result += curr_val
        else:
            result -= curr_val

        prev_val = curr_val

    return result