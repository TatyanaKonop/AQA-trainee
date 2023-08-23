
###Валидация ввода количества товара###
def input_number():
    while True:
        amount = input('Количество: ')   #валидация, что вводится целое число

        try:
            while amount == '0' or int(amount) < 0:
                amount = input('Введите корректное количество товара \nКоличество: ')

            return int(amount)
        except ValueError:
            print('некорректное значение, повторите ввод')

def product_not_empty(product):
    while product == "":  # валидация, что товар указан
        product = input('Добавьте наименование товара:\nТовар: ')
    return product

###Создание списка товаров###
product = input('Добавьте товар и количество (или введите "завершить" для завершения):\nТовар: ')
product_value = {}

while product != "завершить":
    validation_product = product_not_empty(product)
    amount = input_number()
    if validation_product not in product_value.keys(): # создание словаря товар:количество
       product_value[validation_product] = amount
    else:
        prew_amount = product_value.get(validation_product) # суммирование количества повторяющихся товаров
        sum = int(prew_amount) + int(amount)
        product_value[validation_product] = sum
    product = input('Добавьте товар и количество (или введите "завершить" для завершения):\nТовар: ')
print('\n\nCписок товаров:')
for key in product_value:    #печать списка товаров
    print(f'- {key}: {product_value[key]} шт.')









