# Homework_7
#
# Задания 1
#
# Попросите пользователя ввести слово без пробелов. Пока он не введёт правильно, просите его ввести.
# Проверьте, что вы правильно закодили с помощью assert инструкции

# Решение

# while True:
#     a = str(input('Enter word without space: '))
#     if a.find(' ') == -1:
#         break
#     else:
#         input('Enter word without space: ')


# a = str(input('Enter word without space: '))
# assert (a.find(' ') == -1), 'Enter word without space: '
# print(a)


# Задание 2
#
# Делаем из задания функцию «Считываем текст из файла. Посчитываем сколько в нем используется слов (уникальных).»
# Передавайте как аргумент разные файлы. Протестируйте функцию.

# def read_text_from_file(a):
#     a = open("C:\\Users\\Kiev\\Desktop\\sum.py)
#     return a

# def read_text_from_file(file_name):
#     open_file = open(file_name)
#     c = open_file.read().replace(',', '').split()
#     d = list(set(c))
#     return print(len(d))
#
# file_name1 = "C:\\Users\\Kiev\\Desktop\\sum.py"
#
# read_text_from_file(file_name1)

# Задание 3
#
# Пишем функцию, которая выводим второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.

# g = [100, 120, 99, 1, 1, 2, 2, 98]
# b = sorted(set(g))
# print(list(b)[1])
# print(b)

# def second_uprise(incoming_list):
#     sorted_set = sorted(set(incoming_list))
#     sorted_list = list(sorted_set)
#     return print(sorted_list[1])
#
# second_uprise([1, 1, 2, 2, 5, 2])


# Задание 4

# Пишем функцию, которая генерирует песню la-la- la. Функция принимает 3 аргумента:
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце стоит точка, если 1, то в конце стоит «!»

# def song(line_end = 0, num_lines = 3, num_words = 3):
#     # num_lines = int(input("Enter sum of lines for song: "))
#     # num_words = int(input("Enter sum of words for song: "))
#     # line_end = int(input("Enter the end of line, if you enter 0 it will be '.', if 1 - '!': "))
#     if line_end == 0:
#         line_finish = '.'
#     elif line_end == 1:
#         line_finish = '!'
#     else:
#         print('Wrong number')
#
#     word = 'la'
#     count_words_in_lines = (word + '-') * num_words
#     return print('PUTIN'), print(((count_words_in_lines)[:-1] + line_finish + '\n') * num_lines)
#
# song()


