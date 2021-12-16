#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import math
    import sys
except ImportError:
    print("Ошибка загрузки модулей, исправьте код программы!")

a = float(input('Вес (в килограммах) = '))
b = float(input('Рост (в метрах)= '))

def _exit():
    print()
    print('*' * 60)
    print('До свидания!"')
    print('*' * 60)
    sys.exit()

mass_index = a / pow(b, 2)

print('*' * 60)
print(mass_index)
print('*' * 60)
print()
if mass_index < 18.5:
    print('*' * 60)
    print('Недостаточная масса')
    print('*' * 60)
    _exit()
elif 18.5 <= mass_index <= 25:
    print('*' * 60)
    print('Оптимальная масса')
    print('*' * 60)
    _exit()
else:
    print('*' * 60)
    print('Избыточная масса')
    print('*' * 60)
    _exit()

