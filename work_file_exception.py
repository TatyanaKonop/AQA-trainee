import os

class ContainFileError(Exception):
    ###Error occured if file contains more than 100 symbols or empty###
    pass

class CountSymbols(object): # контекстный мененджер по работе с файлам
    def __init__(self, name, method):
        dir_current = os.path.abspath(os.path.dirname(__file__)) # путь  к директории исполняемого текущего файла
        file_path = os.path.join(dir_current,name ) # путь к текстовому файлу
        self.file_object = open(file_path, method, encoding="utf-8")
    def __enter__(self):
        return self.file_object
    def __exit__(self, exc_type, exc_val, exc_tb):
            self.file_object.close()

with CountSymbols('file.txt','r+') as countsym:
    result_symbols = countsym.read()
    length = len(result_symbols)
    print(f'количество символов без пробелов {length}') #в качестве символов учитываются абзацы и пробелы
    try:
        if length > 0 and  length < 100:
            middle = length//2
            if length % 2 == 0: #  !в случае нечетного количества символов первая часть текста больше на один символ
                new_text = result_symbols[:(length - middle-1):-1]+result_symbols[:middle]
            else:
                new_text = result_symbols[:(length - middle-1):-1] + result_symbols[:middle+1]
            countsym.write('\n'+new_text)
        else:
            raise ContainFileError
    except ContainFileError:
        print("файл пустой или слишком большой")











