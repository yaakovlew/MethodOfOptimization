import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

sp.init_printing()

# Построение графиков
x = np.linspace(0, 10, 1000)

y1 = 2 * x
y2 = 16 - 2 * x
y3 = (3 + 2 * x) / 5
y4 = (2 + x) / 2

plt.title("Графики (х2 от х1)")
plt.plot(x, y1, label=r'$y_1: y\leq 2x$')
plt.plot(x, y2, label=r'$y_2: y\leq 16 - 2x$')
plt.plot(x, y3, label=r'$y_3: 5y\geqslant 2x + 3$')
plt.plot(x, y4, label=r'$y_4: 2y\leq 2 + x$')
plt.xlim((0, 8))
plt.ylim((0, 5))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

##Раскраска области решения

y5 = np.minimum(y2, np.minimum(y1, y4))
y6 = y3

plt.fill_between(x, y5, y6, where=y5 > y6, color='grey', alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# Нахождение точек пересечения прямых

sp.var('x y F')

F = 2 * x + 5 * y

y1 = 2 * x
y2 = 16 - 2 * x
y3 = (3 + 2 * x) / 5
y4 = (2 + x) / 2

x_first_intersection_point = sp.solve(sp.Eq(y1, y3), x)[0]
x_second_intersection_point = sp.solve(sp.Eq(y1, y4), x)[0]
x_third_intersection_point = sp.solve(sp.Eq(y2, y3), x)[0]
x_fourth_intersection_point = sp.solve(sp.Eq(y2, y4), x)[0]

y_first_intersection_point = float(y1.subs([(x, x_first_intersection_point)]))
y_second_intersection_point = float(y1.subs([(x, x_second_intersection_point)]))
y_third_intersection_point = float(y2.subs([(x, x_third_intersection_point)]))
y_fourth_intersection_point = float(y2.subs([(x, x_fourth_intersection_point)]))

# Нахождение минимального значения целевой функции и аргументов, при которых достигается минимум функции

min_count_of_function = min(
    F.subs([(x, x_first_intersection_point), (y, y_first_intersection_point)]),
    F.subs([(x, x_second_intersection_point), (y, y_second_intersection_point)]),
    F.subs([(x, x_third_intersection_point), (y, y_third_intersection_point)]),
    F.subs([(x, x_fourth_intersection_point), (y, y_fourth_intersection_point)])
)

print("Минимальное значение функции: ", round(min_count_of_function, 2))

if (F.subs([(x, x_first_intersection_point), (y, y_first_intersection_point)]) == min_count_of_function):
    x_args = x_first_intersection_point
    y_args = y_first_intersection_point
elif (F.subs([(x, x_second_intersection_point), (y, y_second_intersection_point)]) == min_count_of_function):
    x_args = x_second_intersection_point
    y_args = y_second_intersection_point
elif (F.subs([(x, x_third_intersection_point), (y, y_third_intersection_point)]) == min_count_of_function):
    x_args = x_third_intersection_point
    y_args = y_third_intersection_point
elif (F.subs([(x, x_fourth_intersection_point), (y, y_fourth_intersection_point)]) == min_count_of_function):
    x_args = x_fourth_intersection_point
    y_args = y_fourth_intersection_point
else:
    print("Решение не было найдено")
    x_args = 'ø'
    y_args = 'ø'
print("Достигается при x1 = ", float(x_args), "и при x2 = ", y_args)
