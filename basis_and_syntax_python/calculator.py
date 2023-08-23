def input_number(): #ввод числа
    while True:
        number = input('введите число:')
        try:
            return float(number)
        except ValueError:
            print('некорректные данные')

def input_sign(): #ввод знака операции
    while True:
        sing = input('введите знак операции:')
        if sing in ('+', '-', '*', '/'):
            return sing
        else:
            print('некорректные данные')
number_1 = input_number()
sing_operation = input_sign()
number_2 = input_number()
### Выполнение арифметической операции
if sing_operation == '+':
    result = number_1 + number_2
    print(f' {result}')
elif sing_operation == '-':
    result = number_1 - number_2
    print(f' {result}')
elif sing_operation == '*':
    result = number_1 * number_2
    print(f'{result}')
else:
    try:
        result = number_1 / number_2
        print(f' {result}')
    except ZeroDivisionError:
        print('деление на ноль запрещено')
