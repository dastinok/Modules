'''Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
'''

'''Добавьте в модуль с загадками функцию, которая хранит словарь списков. 
Ключ словаря - загадка, значение - список с отгадками. 
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки. 
'''

'''Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). 
Функция формирует словарь с информацией о результатах отгадывания. 
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
Для формирования результатов используйте генераторное выражение.
'''

from package.module_seminar_4 import *


#print(rid('Маленькие домики по улице бегут,Мальчиков и девочек домики везут.', ['машины', 'машинки'], 5))
get_puzzles()
result()

