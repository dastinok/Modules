'''Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
'''


def get_riddle(puzzle: str, answer: list, count: int = 5):
    print(f'Загадка - {puzzle}')
    effort = 1
    while count:
        user_answer = input('Ответ: ').lower()
        effort = 1

        if user_answer in answer:
            return effort

        effort += 1
        count -= 1
    return 0

def get_puzzles():
    puzzles = {'Маленькие домики по улице бегут,Мальчиков и девочек домики везут.':
                ['машины', 'машинки'],
                'Висит груша нельзя скушать': ['лампочка'],
                'Зимой  и летом одним цветом': ['елка', 'сосна']}

    for puzzle, answer in puzzles.items():
        fun_2(puzzle, get_riddle(puzzle,answer))

    print(_result_dict)

_result_dict = {}

def fun_2(puzzle: str, number: int = 0):
    _result_dict[puzzle] = number

def result():
    for puzzle, item in _result_dict.items():
        print(f'Загадка - {puzzle}, угадана с {item} попытки')