'''
Самостоятельная работа по уроку "Рекурсия"
'''

#создаю функцию get_multiplied_digits принимающую переменную number(целое число)
def get_multiplied_digits(number):
    #для работы преобразую number в текст представление
    str_number = str(number)
    #записываю в переменную first в числовом представлении первую цифру числа 40203 (0- индекс первого числа)
    first = int(str_number[0])
       # если длина строки больше 1
    if len(str_number) > 1:
       #number=Fist*текущее число. Параметр тек числа передаем в фуекцию
       number = first * get_multiplied_digits(int(str_number[1:]))
    else:
        #возврат оставшуюся цифру(можно любую)
        first
    #возвражаем результат number
    return (number)

result = get_multiplied_digits(40203)
print(result)


