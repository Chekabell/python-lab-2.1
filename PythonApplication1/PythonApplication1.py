import itertools
from math import trunc
from time import perf_counter
from itertools import filterfalse
import mymodule

#Функция обработчик ввода
def input_func(a):
    #Проверка на пустую строку
    if a != "":
        try:
            #Проверка на число или строку с помощью перехвата исключения
            float(a)
            a = str(a)
            #Проверка является ли число десятичным или целочисленным
            if a.isdigit() is False:
                a = float(a)
                #Проверка является ли число положительным
                if a >= 0:
                    return a
                print("It's negative.")
            else:
                print("It's int.")
        except:
            #Разделение строки на отдельные символы
            a = list(a)
            #Сортировка маленьких английских букв
            a = list(filterfalse(lambda x: x <= 'a' or x >= 'z', a))
            #Сортировка английских согласных букв
            a = "".join(list(filterfalse(lambda x: x=='a' or x=='e' or x=='i' or x=='o' or x=='u',a)))
            b = len(a)
            #Проверка на то, что строка не отсталась пустой
            if b==0:
                return None
            return a
    else:
        print("Empty string.\n")
        return None


#Функция декоратор
def decorator_func(function): 
    def wrapper(spisok):
        #Начало подсчёта времени
        t_start = perf_counter()
        a = function(spisok)
        #Вычисление итогового времени выполнения функции
        t_end = perf_counter() - t_start
        #Проверка на то, что числа былы введены и минимум нашёлся
        if a[0]!=10**10:
            print("\n",a[0],"- minimal value\n")
        else:
            print("\nNot numbers in list\n")
        
        #Проверка на то, что строки были введены
        if a[1]!=0:
            print("\n",a[1],"- number of symbols\n")
        else:
            print("\nNot strings in list\n")
        
        #Усечение всех дробных чисел до целочисленных значений и заполнение списка для их выведения
        sps = []
        for i in range(len(spisok)):
            if type(spisok[i]) is float:
                sps.append(trunc(spisok[i]))
        if len(sps):
            print("\nPositive truncated numbers: ",sps)
        #Замена в каждой строке на заглавную всех букв, кроме 3-ей
        #Дополнительный список нужен, чтобы не выводить лишние элементы при показе результата
        sps = []
        for i in spisok:
            if type(i) is str:
                count = 0
                r=''
                for j in range(len(i)):
                    if count<2:
                        r+=i[j].upper()
                        count+=1
                    else:
                        r+=i[j]
                        count=0
                spisok[spisok.index(i)]=r
                sps.append(r)
        if len(sps)!=0:
            print("\nThis is work with string: ",sps)
        print("\nExecution time of the calculator function", t_end, "\n")
        return a
    return wrapper


@decorator_func
def calculator(spisok):
    #Переменная minimum нужна для поиска наименьшего числа, а lenght для подсчёта количества пропущенных букв
    minimum = 10**10
    lenght = 0
    for i in spisok:
        if type(i) is str:
            lenght+=len(i)
        if type(i) is float:
            if i<minimum:
                minimum=i
    return minimum, lenght


#Ввод пользователем данных
spisok=[]
while 1:
    print("Enter: ")
    a = input()
    #Если пользователь ввёл команду "end", то ввод прекращается и вызывается функция вычислитель
    if a=="end":
        calculator(spisok)
        break
    a = input_func(a)
    #Если функция обработчик не возвращает None, то мы добавляем новое значение в список
    if a != None:
        spisok.append(a)


help(mymodule)


rand_sp = []
for i in range(5):
    rand_sp.append(mymodule.rand1(46,87))
    rand_sp.append(mymodule.rand2(4,85,4))
print(rand_sp)

rand_sp_fin = []
for i in rand_sp:
    rand_sp_fin.append(input_func(i))
print(rand_sp)
    
    

    