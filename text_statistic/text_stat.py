import os
import string


def text_stat(filename: str) -> dict:
    if not isinstance(filename, str):
        return {'error': 'Неверный тип аргумента(имени файла) - ожидался str, а не {}'.format(type(filename))}
    latin_letters = string.ascii_letters
    cyrillic = "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = {i: 0 for i in latin_letters + cyrillic}
    paragraph_amount = 0
    bilingual_word_amount = 0
    word_amount = 0
    latin = 0
    cyril = 0
    letters_words = {i: 0 for i in latin_letters + cyrillic}
    check_letters = set()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, filename + '.txt')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                if line[0] == '\t':
                    paragraph_amount += 1
                words = list(filter(lambda x: x != '' and x != '\n', line.split(' ')))
                word_amount += len(words)
                for word in words:
                    for c_letter in [c for c in word if c in latin_letters or c in cyrillic]:
                        result[c_letter] += 1
                        if c_letter not in check_letters:
                            letters_words[c_letter] += 1
                            check_letters.add(c_letter)
                        if latin == 0 and c_letter in latin_letters:
                            latin = 1
                        if cyril == 0 and c_letter in cyrillic:
                            cyril = 1
                    if latin == 1 and cyril == 1:
                        bilingual_word_amount += 1
                    check_letters.clear()
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
            result[i] = (result[i], letters_words[i] / word_amount)
    return {
        **result,
        'word_amount': word_amount,
        'paragraph_amount': paragraph_amount,
        'bilingual_word_amount': bilingual_word_amount
    }
