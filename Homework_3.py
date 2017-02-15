# Homework 2/15/2017
#
# Задание 1
#
# Напишите программу по следующему описанию:
#
# a. двум переменным присваиваются числовые значения из командной строки;
#
# b. если значение первой переменной больше второй, то найти разницу значений переменных
#
# (вычесть из первой вторую), результат связать с третьей переменной;
#
# c. если первая переменная имеет меньшее значение, чем вторая, то третью переменную
#
# связать с результатом суммы значений двух первых переменных;
#
# d. во всех остальных случаях, присвоить третьей переменной значение первой переменной;
#
# e. вывести значение третьей переменной на экран.

# 1. Result:

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a > b:
    c = (a-b)
elif a < b:
    c = (a+b)
else:
    c = a

print(c)

# Задание 2 (если сможете, постарайтесь придумать)
#
# 1) Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
#
# 2) Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.

# 2.1)
d = 0
while d <= 10:
     print(d)
     d = d + 1

# 2.2)
g = 20
while g > 0:
    print(g)
    g = g - 1

# 3.
while True:
    print("Type 'quit' to exit")
    phrase = input("Your message: ")
    if phrase == "quit" or phrase == "exit" or phrase == "bye":
        break
    elif phrase == "Hello" or phrase == "Hi":
        print("Hi! what's up?")
    elif phrase == "What's your name?":
        print("I am Aleksandr")
    elif phrase == "Good, how are you?":
        print("Great, thanks!")
    elif phrase == "Nice to see you":
        print("Me too!")
    elif phrase == "Where are you heading":
        print("Python classes")
    elif phrase == "Do you like it? ":
        print("Sure, it's the best high-level programming language")
    elif phrase == "Ok, I should go home":
        print("OK, Have a good classes, Bye! ")
    else:
        print("I don't understand you")

