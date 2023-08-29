import os
from contextlib import contextmanager

class ContainFileError(Exception):
    ###Error occured if file contains more than 100 symbols or empty###
    pass

@contextmanager
def my_context(name, method):
    dir_current = os.path.abspath(os.path.dirname(__file__)) # путь  к директории исполняемого текущего файла
    file_path = os.path.join(dir_current, name) # путь к текстовому файлу
    file_object = open(file_path, method, encoding="utf-8")
    try:
        result_symbols = file_object.read()
        length = len(result_symbols)
        print(f'количество символов без пробелов {length}')  # в качестве символов учитываются абзацы и пробелы

        if length > 0 and length < 100:
            middle = length // 2
            if length % 2 == 0:  # !в случае нечетного количества символов первая часть текста больше на один символ
                new_text = result_symbols[:(length - middle - 1):-1] + result_symbols[:middle]
            else:
                new_text = result_symbols[:(length - middle - 1):-1] + result_symbols[:middle + 1]
        else:
            raise ContainFileError
        yield file_object, new_text
    except ContainFileError:
        print("файл пустой или слишком большой")
        yield file_object, None
    finally:
        file_object.close()
with my_context("file.txt", 'r+') as (file_object, new_text):
    if new_text:
        file_object.write('\n' + new_text)
    else:
        pass














