from math import trunc
import math

#Функция обработчик ввода
def input_func(a):
    #Проверка на пустую строку
    if a != "":
        try:
            #Проверка на число или строку с помощью перехвата исключения
            float(a)
            
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
            b=len(a)
            
            #Вложенные циклы, которые позволяют проверить строку на соответсвие нужным данным
            for i in range(b):
                for j in range(b):
                    #Проверка на вхождение в английский алфавит и маленькие буквы
                    if 'a' <= a[j] <= "z":
                        #Проверка на согласные и гласные буквы
                        if a[j]=='a' or a[j]=='e' or a[j]=='i' or a[j]=='o' or a[j]=='u':
                            print(a[j],"- this isn't consonant letter")
                            a.pop(j)
                            b=len(a)
                            break   
                        else:
                            if a[j].isupper():
                                print(a[j],"- this is up register")
                                a.pop(j)
                                b=len(a)
                                break
                    else:
                        print(a[j],"- this is not english word or up register")
                        a.pop(j)
                        b=len(a)
                        break
            #Проверка на то, что строка не отсталась пустой
            if b==0:
                return None
            #Объединение и возвращение строки
            return "".join(a)
    else:
        print("Empty string.\n")
        return None


#Функция декоратор
def decorator_func(function): 
    def wrapper(spisok):
        a = function(spisok)
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
        
        #Подсчёт количества положительных чисел. В моих условиях достаточно подсчитать просто кол-во чисел
        sps = []
        for i in range(len(spisok)):
            if type(spisok[i]) is float:
                spisok[i]= math.trunc(spisok[i])
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
        return a
    return wrapper


@decorator_func
def calculate(spisok):
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
    #Если пользователь ввёл команду "end", то ввод прекращается и вызывается функция декоратор
    if a=="end":
        calculate(spisok)
        break
    a = input_func(a)
    #Если функция обработчик не возвращает None, то мы добавляем новое значение в список
    if a != None:
        spisok.append(a)
            

    