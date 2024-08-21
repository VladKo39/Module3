""" Домашняя работа по уроку "Пространство имён\""""
#Присваиваем переменной счётчика  значение 0
calls=0
'''
Функция count_calls подсчитывающая вызовы остальных функций.
'''
#Создаем функцию счётчика
def count_calls():
    #Присваиваем переменной calls Global для отражения счётчика далее
    global calls
    #при вызове функции увеличение на 1
    calls+=1
    #Функция должна вернуть значение Calls счётчика
    return calls
'''
Функция string_info принимает аргумент - строку и возвращает кортеж из:
   длины этой строки, 
   строку в верхнем регистре, 
   строку в нижнем регистре.
'''
def string_info (value):
    value=(len(value),value.upper(),value.lower())
    #запуск счётчика
    count_calls()
    ##Функция должна вернуть значение Value Длина строки, нижн.регистр, верх.регистр.
    return (value)
'''Функция is_contains принимает два аргумента: 
   строку и список, 
   и возвращает True, если строка находится в этом списке,
    False - если отсутствует.
    Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
'''
def is_contains (value,list):
    #Новый список List= перебираем map строки str и
    # переводим методом Lower список List в верх регистр
    list = map(str.lower,list)
    #Если значение Value в верх.регистре Lower находится в списке List
    if value.lower() in list:
         # Флаг = Истина
         flag=True
    # Иначе
    else:
        # Флаг = Ложь
        flag=False
    # запуск счётчика
    count_calls()
    ##Функция должна вернуть Истина,Ложь
    return flag

#Вывод на консоль с исходными значениями
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)