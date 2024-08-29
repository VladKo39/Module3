'''
Дополнительное практическое задание по модулю*
Дополнительное практическое задание по модулю: "Подробнее о функциях."

result = calculate_structure_sum(data_structure)
print(result)

Выходные данные (консоль):
99
'''
#Создаю функцию calcul_all для подсчёта всех данных
#c параметром data_structure
def calculate_structure_sum(data_structure):
    sum_ = 0
    #
    #если элемент в data_structure является словарем
    if isinstance(data_structure, dict):
        #перебираем словарь
        for key,value in data_structure.items():
            # к cum_ прибавляем возвратное значение calculate_structure_sum ключа
            sum_ += calculate_structure_sum(key)
            # к cum_ прибавляем возвратное значение calculate_structure_sum значения по ключу
            sum_ += calculate_structure_sum(value)
    # если элемент в data_structure является строкой, кортежем, множеством
    elif isinstance(data_structure,(list,tuple,set)):
        # перебираем словарь
        for element_ in data_structure:
            # к sum_ прибавляем возвратное значение calculate_structure_sum элемента
            sum_ += calculate_structure_sum(element_)
    # если data_structure является целым числом или числом с плавающей запятой
    elif isinstance(data_structure,(int,float)):
        # к sum_ прибавляем возвратное значение data_structure
        sum_ += data_structure
    # если data_structure является строкой
    elif isinstance(data_structure,str):
        # к sum_ прибавляем возвратное значение кол элементов data_structure
        sum_ += len(data_structure)
    return sum_

print(f'{"*"*40}')

data_structure=[
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]

result_=(calculate_structure_sum(data_structure))
print(f'Результат : {result_}')
