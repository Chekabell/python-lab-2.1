"""
Справка модуля mymodule.
Данный модуль содержит две функции (rand1(x,y) и rand2(x,y,z)) для выполнения 
20 варианта задания с использованием подключаемого модуля random.
"""
from random import random, randint, randrange

def rand1(x,y):
    """
    Справка функции rand1.
    Функция для выполнения первого задания 1: random()*randint (46, 87)
    """
    return random()*randint(x,y)

def rand2(x,y,z):
    """
    Справка функции rand1.
    Функция для выполнения первого задания 2: float(randrange(4, 85, 4))
    """
    return float(randrange(x,y,z))