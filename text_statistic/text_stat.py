import string
from pprint import pprint


def text_stat(filename):
    latin_letters = string.ascii_letters
    cyrillic = "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = {i: 0 for i in latin_letters + cyrillic}
    paragraph_amount = 0
    bilingual_word_amount = 0
    word_amount = 0
    latin = 0
    cyril = 0
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                if line[0] == '\t':
                    paragraph_amount += 1
                words = list(filter(lambda x: x != '' and x != '\n', line.split(' ')))
                print(words)
                word_amount += len(words)
                for word in words:
                    for uniqie_letter in {c for c in word if c in latin_letters or c in cyrillic}:
                        result[uniqie_letter] += 1
                        if latin == 0 and uniqie_letter in latin_letters:
                            latin = 1
                        if cyril == 0 and uniqie_letter in cyrillic:
                            cyril = 1
                    if latin == 1 and cyril == 1:
                        bilingual_word_amount += 1
                    latin = 0
                    cyril = 0
                line = f.readline()
    except MemoryError:
        return {'error': 'Ошибка нехватки памяти'}
    except (FileNotFoundError, PermissionError, OSError):
        return {'error': 'Ошибка при открытии файла: файл не найден, нет прав доступа или файл заблокирован'}
    except UnicodeDecodeError:
        return {'error': 'Ошибка при открытии файла: невозможно распознать кодировку'}
    except ValueError:
        return {'error': 'Ошибка при открытии файла: файл поврежден или имеет некорректный формат'}
    if word_amount != 0:
        for i in result:
            result[i] = (result[i], result[i] / word_amount)
    return {
        **result,
        'word_amount': word_amount,
        'paragraph_amount': paragraph_amount,
        'bilingual_word_amount': bilingual_word_amount
    }


if __name__ == "__main__":
    f_name = input()
    pprint(text_stat(f_name))
# todo: подсчет букв - всех, не уникальных. Доля слов с буквами уникальными. Возможное решение: отдельный словарь для уникальных слов для каждой буквы.
# todo: после этого просто для каждый буквы посчитать her_amount/ word amount. 
