from sympy import *
import numpy as np
import matplotlib.pyplot as plt

print("""Нарушение этих правил ведет к падению программы:

 Программа принимает функции в виде 'y - kx'

 В уравнении должны участвовать две буквы.
 Разрешаются только буквы X и Y, регистер и пробелы не важны
 Введите уравнение так, чтобы правая часть была равна нулю
 Умножение записывается Только символом '*'
 Скобки использовать МОЖНО
 Степень записывается в таком виде: a**n,
где 'a' - основание, 'n' - степень

Хороший пример: '2*y-4*x+7'
Плохой пример: '4z-12 = 3i'
""")

x = Symbol('x')
y = Symbol('y')

system = ()

try:
	iters = int(input("Введите количество уравнений в системе (1 если это не система): "))
except:
	print("Что-то сломалось, будет просчитано только одно уравнение")
	iters = 1

for i in range(iters):
    inp = input("Введите уравнение: ").lower()
    inp = eval(inp)
    system = system + (inp,)

sol = str(solve(system, (y)))
if sol != "":

    y1 = lambda x: eval(sol)

    fig, ax = plt.subplots()

    x_vals = np.linspace(-100, 100, 1000)
    for i in x_vals:
        Y = y1(i)
        if isinstance(Y, dict):
            Y = Y[y]
            if not "I" in str(Y):
                plt.plot(i, Y, "bo")
        if isinstance(Y, list):
            for j in Y:
                Y = j[0]
                if not "I" in str(Y):
                    plt.plot(i, Y, "bo")
    

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
else:
    print("В данный момент калькулятор не умеет считать такое")
