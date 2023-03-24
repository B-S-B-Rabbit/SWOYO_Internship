from unittest import TestCase, main
from text_statistic.text_stat import text_stat


class MyTestCase(TestCase):
    def test_not_open(self):
        self.assertEqual(text_stat('trouble_file'),
                         {'error': 'Ошибка при открытии файла: файл не найден, нет прав доступа или файл заблокирован'})

    def test_wrong_codec(self):
        self.assertEqual(text_stat('wrong_codec'),
                         {'error': 'Ошибка при открытии файла: невозможно распознать кодировку'})

    def test_empty_file(self):
        self.assertEqual(text_stat('empty_file'),
                         {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
                          'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
                          'w': 0, 'x': 0, 'y': 0, 'z': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                          'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
                          'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'а': 0, 'б': 0, 'в': 0,
                          'г': 0, 'д': 0, 'е': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0,
                          'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0,
                          'щ': 0, 'ъ': 0, 'ы': 0, 'ь': 0, 'э': 0, 'ю': 0, 'я': 0, 'А': 0, 'Б': 0, 'В': 0, 'Г': 0,
                          'Д': 0, 'Е': 0, 'Ж': 0, 'З': 0, 'И': 0, 'Й': 0, 'К': 0, 'Л': 0, 'М': 0, 'Н': 0, 'О': 0,
                          'П': 0, 'Р': 0, 'С': 0, 'Т': 0, 'У': 0, 'Ф': 0, 'Х': 0, 'Ц': 0, 'Ч': 0, 'Ш': 0, 'Щ': 0,
                          'Ъ': 0, 'Ы': 0, 'Ь': 0, 'Э': 0, 'Ю': 0, 'Я': 0, 'word_amount': 0, 'paragraph_amount': 0,
                          'bilingual_word_amount': 0})

    def test_one_word_file_all_letters(self):
        self.assertEqual(text_stat('one_word_file_all_letters'),
                         {'a': (1, 1.0), 'b': (1, 1.0), 'c': (1, 1.0), 'd': (1, 1.0), 'e': (1, 1.0), 'f': (1, 1.0),
                          'g': (1, 1.0), 'h': (1, 1.0), 'i': (1, 1.0), 'j': (1, 1.0), 'k': (1, 1.0), 'l': (1, 1.0),
                          'm': (1, 1.0), 'n': (1, 1.0), 'o': (1, 1.0), 'p': (1, 1.0), 'q': (1, 1.0), 'r': (1, 1.0),
                          's': (1, 1.0), 't': (1, 1.0), 'u': (1, 1.0), 'v': (1, 1.0), 'w': (1, 1.0), 'x': (1, 1.0),
                          'y': (1, 1.0), 'z': (1, 1.0), 'A': (1, 1.0), 'B': (1, 1.0), 'C': (1, 1.0), 'D': (1, 1.0),
                          'E': (1, 1.0), 'F': (1, 1.0), 'G': (1, 1.0), 'H': (1, 1.0), 'I': (1, 1.0), 'J': (1, 1.0),
                          'K': (1, 1.0), 'L': (1, 1.0), 'M': (1, 1.0), 'N': (1, 1.0), 'O': (1, 1.0), 'P': (1, 1.0),
                          'Q': (1, 1.0), 'R': (1, 1.0), 'S': (1, 1.0), 'T': (1, 1.0), 'U': (1, 1.0), 'V': (1, 1.0),
                          'W': (1, 1.0), 'X': (1, 1.0), 'Y': (1, 1.0), 'Z': (1, 1.0), 'а': (1, 1.0), 'б': (1, 1.0),
                          'в': (1, 1.0), 'г': (1, 1.0), 'д': (1, 1.0), 'е': (1, 1.0), 'ж': (1, 1.0), 'з': (1, 1.0),
                          'и': (1, 1.0), 'й': (1, 1.0), 'к': (1, 1.0), 'л': (1, 1.0), 'м': (1, 1.0), 'н': (1, 1.0),
                          'о': (1, 1.0), 'п': (1, 1.0), 'р': (1, 1.0), 'с': (1, 1.0), 'т': (1, 1.0), 'у': (1, 1.0),
                          'ф': (1, 1.0), 'х': (1, 1.0), 'ц': (1, 1.0), 'ч': (1, 1.0), 'ш': (1, 1.0), 'щ': (1, 1.0),
                          'ъ': (1, 1.0), 'ы': (1, 1.0), 'ь': (1, 1.0), 'э': (1, 1.0), 'ю': (1, 1.0), 'я': (1, 1.0),
                          'А': (1, 1.0), 'Б': (1, 1.0), 'В': (1, 1.0), 'Г': (1, 1.0), 'Д': (1, 1.0), 'Е': (1, 1.0),
                          'Ж': (1, 1.0), 'З': (1, 1.0), 'И': (1, 1.0), 'Й': (1, 1.0), 'К': (1, 1.0), 'Л': (1, 1.0),
                          'М': (1, 1.0), 'Н': (1, 1.0), 'О': (1, 1.0), 'П': (1, 1.0), 'Р': (1, 1.0), 'С': (1, 1.0),
                          'Т': (1, 1.0), 'У': (1, 1.0), 'Ф': (1, 1.0), 'Х': (1, 1.0), 'Ц': (1, 1.0), 'Ч': (1, 1.0),
                          'Ш': (1, 1.0), 'Щ': (1, 1.0), 'Ъ': (1, 1.0), 'Ы': (1, 1.0), 'Ь': (1, 1.0), 'Э': (1, 1.0),
                          'Ю': (1, 1.0), 'Я': (1, 1.0), 'word_amount': 1, 'paragraph_amount': 1,
                          'bilingual_word_amount': 1}
                         )


if __name__ == '__main__':
    main()