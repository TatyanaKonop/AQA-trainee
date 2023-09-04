import sqlite3
import re
import json

class ErrorInput(Exception):
    pass

class ErrorInputKeyValue(Exception):
    pass

class DataBase:
    table = [
        'id integer PRIMARY KEY AUTOINCREMENT',
        'name TEXT',
        'author TEXT',
        'publish_year TEXT',
        'ISBN TEXT'
    ]

    def __init__(self, database_path: str):
        self.db = sqlite3.connect(database_path)
        self.cursor = self.db.cursor()
    # создание таблицы
    def create_table(self, table_name):
        query = f'''CREATE TABLE IF NOT EXISTS {table_name}(
                    {DataBase.table[0]},
                    {DataBase.table[1]},
                    {DataBase.table[2]},
                    {DataBase.table[3]},
                    {DataBase.table[4]}
                    )'''
        self.execute_query(query)

    # заполнение данных в таблице
    def add_user_entry(self,  table_name, entities):
        query = f'''INSERT INTO {table_name}(name, author, publish_year, ISBN)
                            VALUES(?, ?, ?, ?) '''
        self.execute_query(query, entities)

    # изменение данных в таблице
    def add_column(self, table_name, new_value, key_value, column):
        set_sum = ''
        for i in range(len(column)):
            set_expression = str(column[i]) + ' = ' + "'" + str(new_value[i]) + "'" + ', '
            set_sum = set_sum +  set_expression
        set_sum = set_sum[:-2]
        query = f'''UPDATE {table_name} SET {set_sum} WHERE ISBN = '{key_value}' '''
        self.execute_query(query)

    # выборка всех данных из таблицы
    def select_data_all(self, table_name):
        query = f'''SELECT * FROM {table_name}'''
        self.execute_query(query)
        rows = self.cursor.fetchall()
        # for i in rows:  #если данные надо вывести на печать
        #     print(i, sep=" ", end=" " '\n')
        return rows

    # выборка  определеного столбца из таблицы
    def select_data(self, table_name, column):
        query = f'''SELECT {column} FROM {table_name}'''
        self.execute_query(query)
        rows = self.cursor.fetchall()
        return rows

    # выборка  данных по значению столбца
    def select_data_key_value(self, table_name, column, key, key_value):
        query = f'''SELECT {column} FROM {table_name} WHERE {key} = '{key_value}' '''
        self.execute_query(query)
        rows = self.cursor.fetchall()
        for i in rows:  #если данные надо вывести на печать
            print(i, sep=" ", end=" " '\n')



    #удаление данных из таблицы
    def delete_data(self, table_name, key_value):
        query = f'''DELETE FROM {table_name} WHERE ISBN = '{key_value}' '''
        print(query)
        self.execute_query(query)

    #Выполение запроса
    def execute_query(self, query, *d):
        self.cursor.execute(query, *d)
        self.db.commit()


# создание таблицы
def create_entry_db(table_name='booklist', path='../booklist.db'):
    db = DataBase(path)
    db.create_table(table_name)


# соединение с базой данных
def open_db():
    db = DataBase('../booklist.db')
    return db

#Проверка есть строка с таким значением ячейки
def check_element(key_value, key):
    column = key
    db = open_db()
    key_value_list = db.select_data('booklist', column)
    key_value = tuple(map(str, key_value.split()))
    if key_value in key_value_list:
        return key_value
    else:
        raise ErrorInputKeyValue

# Проверка на соостветствие шаблону
def check_string(elems):
    pattern = re.compile(r'\d{3}-\d-\d{3}-\d{5}-\d') #978-5-400-06256-6 образец
    while True:
        try:
            if pattern.match(elems):
                return elems
            else:
                raise ErrorInputKeyValue
        except ErrorInputKeyValue:
            elems = input("Повторите ввод согласно образца (978-5-400-06256-6): ")


def row_to_dict(i): # преобразование из кортежа в словарь
    return {"id": i[0], "name": i[1], "author": i[2], "publish_year": i[3],  "ISBN": i[4]}


#запись данных в JSON файл
def json_data_file(rows):
    dict_row = []
    for i in rows:  # если данные надо вывести на печать
        dict_row.append(row_to_dict(i))  # преобразование из кортежа в словарь
# Запись в файл JSON
    with open("data.json", "w") as f:
        json.dump(dict_row, f)  # преобразование из словаря в JSON формат

#  простая авторизация
def log_in_simple():
    while True: # повторение ввода данных пока не будет совпадения
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        with open('password.txt','r') as f:
            users = f.read().splitlines() # чтение информации с файла
            for user in users:
                args = user.split(':')
                if login == args[0] and password == args[1]: # сравнение введенных данных и данных из файла
                    return False
            else:
                print("Неверный логин и пароль")

def CRUD():
    log_in_simple()
    db = open_db()
    while True:
        try:
            # ввод данных от пользователя: выбор операции для выполения
            operation = input("Введите номер  операции, которую хотите выполнить: 1 - ввод данных о книге,"
               " 2 - корректировка данных о книге, 3 - просмотр списока книг,"
               " 4- удаление информации о книге: ")
            list_input = ["наименование книги", " фамилию имя отчетство автора (пример K.N.Hlew)", "год издания", "ISBN по образцу xxx-x-xxx-xxxxx-x"]
            list_table = ['name', 'author', 'publish_year', 'ISBN']
            if operation == '1': # блок для ввода данных в таблицу
                #ввод данных о книге
                entities = tuple()
                for i in list_input:
                    elems = tuple(map(str, input(f"Введите {i} ").splitlines()))
                    if  i == "ISBN по образцу xxx-x-xxx-xxxxx-x": #  проверка на ввод ISBN по образцу 978-5-400-06256-6
                        elems = ''.join(elems)
                        elems = check_string(elems)
                        elems = tuple(map(str, elems.split()))
                    entities = entities + elems
                db.add_user_entry('booklist', entities)
                break

            elif operation == '2': # блок для изменения данных в таблице
                column = tuple()
                new_value = tuple()
                #ввод данных для измениня таблицы
                for i in list_table:
                    elems = tuple(map(str, input(f"Введите новое значение для столбца {i} ").splitlines()))

                    if i == 'ISBN':  # проверка на ввод ISBN по образцу 978-5-400-06256-6
                        elems = ''.join(elems)
                        elems = check_string(elems)
                        elems = tuple(map(str, elems.split()))

                    new_value = new_value + elems # новые значения для столбцов
                    # если значение столца введено, наименование столбца с новым значением передаются в метод
                    # если значение для указанного столбца не введено, значит информация в их не подлежит изменению
                    if elems:
                        elems_column = tuple(map(str, i.splitlines()))
                        column = column + elems_column
                while True:  # при вводе неверного ISBN пользователь должен повторить попытку ввода
                    try:
                        key_value = input("Введите ISBN книги, данные по которой хотите изменить ")
                        check_element(key_value, key = 'ISBN')
                        break
                    except ErrorInputKeyValue:
                        print("Книги с таким ISBN нет")
                db.add_column('booklist', new_value, key_value, column)
                break

            elif operation == '3': # блок для вывода данных

                    while True:
                        try:
                            column = input('Введите имя столбца по которому хотите получить информацию (name, author, publish_year, ISBN):')

                            if column in ('name', 'author', 'publish_year', 'ISBN'):
                                break
                            else:
                                raise ErrorInputKeyValue

                        except ErrorInputKeyValue:
                            print("Такого значения нет, повторите ввод")
                    while True:
                        try:
                            key = input('Введите имя столбца по которому хотите выбрать информацию (name, author, publish_year, ISBN):')

                            if key  in ('name', 'author', 'publish_year', 'ISBN'):
                                break
                            else:
                                raise ErrorInputKeyValue
                        except ErrorInputKeyValue:
                            print("Такого значения нет, повторите ввод")

                    while True:  # при вводе неверного значения пользователь должен повторить попытку ввода
                        try:
                            key_value = input(f"Введите значение столбца {key} по которому хотите произвести выборку: ")
                            check_element(key_value, key)
                            break
                        except ErrorInputKeyValue:
                            print("Такого значения нет, повторите ввод")

                    db.select_data_key_value('booklist', column, key, key_value)
                    break

            elif operation == '4': #  блок для удаления данных из таблицы
                while True: # при вводе неверного ISBN пользователь должен повторить попытку ввода
                    try:
                        key_value = input("Введите ISBN книги, данные по которой хотите удалить ")
                        check_element(key_value, key = 'ISBN')

                        break
                    except ErrorInputKeyValue:
                        print("Книги с таким ISBN нет")
                db.delete_data('booklist', key_value)
                break
            else:                          #  некорректный выбор номера операции
                raise ErrorInput
                print("Введите корректное значение")

        except ErrorInput:
            print("ВВедите корректное значение")

# запуск программы для CRUD запросов
CRUD()

#Select все данных в базе данных с записью данных в JSON файле
db = open_db()
rows = db.select_data_all('booklist') #вывод всех данных из таблицы
json_data_file(rows)







