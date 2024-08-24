'''
Самостоятельная работа по уроку "Произвольное число параметров".
Цель: закрепить знание использования параметров *args/ **kwargs на практике.
Задача "Однокоренные":
Напишите функцию single_root_words, которая принимает
одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит одно из этих слов.
После вернуть список same_words в качестве результата своей работы.
'''

#Создаю функцию single_root_words принимает 1 обязательльное слово в  root_word
#  и неограниченную последовательность в кортеж root_word
def single_root_words(root_word,*other_words):
    #создаю список для сбора слов по условию задания
    same_words=[]
    #Задаю цикл с проходам по элементам new_name кортежа other_words
    for new_name in (other_words):
        #если значение root_word в верхнем регистре входит в значение new_name в верх регистре
        if root_word.upper() in new_name.upper():
           #Добавляем элемент в список same_words
           same_words.append(new_name)
        # если значение new_name в верхнем регистре входит в значение root_word в верх регистре
        if new_name.upper() in root_word.upper():
            # Добавляем элемент в список same_words
           same_words.append(new_name)
    #Как результат возвращаем созданный список
    return same_words

result1=single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result2=single_root_words('rich','richiest', 'orichalcum', 'cheers', 'richies')

print(f'{"*"*25}Вывод рерультатов{"*"*25}')
print(f'Результат 1: {result1}')
print(f'Результат 2: {result2}')