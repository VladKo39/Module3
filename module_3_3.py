''''
Самостоятельная работа по уроку "Распаковка позиционных параметров".
Домашнее задание по уроку "Распаковка позиционных параметров".

'''
print(f'{'*'*15}Выполнение По заданию 3_2{'*'*15}')
print(f'{'*'*15}1 задание{'*'*15}')
'''
1.Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
'''
def print_params(a = 1, b = 'строка', c = True):

    return(a,b,c)

print(f'Список с параметрами  \n'
      f'без аргументов         : {print_params()}')
print(f'Список с изменениями b : {print_params(b = 25)}')
print(f'Список с изменениями c : {print_params(c = [1,2,3])}')

print(f'{'*'*15}2 задание{'*'*15}')
'''
2.Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
'''
values_list=[1,'Осень',False]
values_dict={"a":'Победа',
             "b" : True,
             "c": 10 }
print(f'Список с изменениями \n'
      f'с распаковкой списка   : {print_params(*values_list)}')
print(f'Список с изменениями \n'
      f'из словоря с распаковкой: {print_params(**values_dict)}')

print(f'{'*'*15}3 задание{'*'*15}')
'''
3.Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)
'''
values_list_2 = [54.32, 'Строка']
print(print_params(*values_list_2,42))
