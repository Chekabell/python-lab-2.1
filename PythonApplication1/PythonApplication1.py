import calendar, sys, cmath
import re
 
# Является ли год високосным
print(calendar.isleap(2000))
print(calendar.isleap(2100))
 
# Строка заголовков дней недели
print(calendar.weekheader(2))
 
# weekday() возвращает индекс дня недели для заданной даты
june3 = calendar.weekday(2023, 6, 3)
wh = calendar.weekheader(9).split()
print(wh[june3])


print(sys.getwindowsversion())

print(sys.getdefaultencoding())

print(sys.getallocatedblocks())


compNum = complex('1-2j')

print(compNum)

re = compNum.real
im = compNum.imag

print(cmath.polar(compNum))

print(cmath.exp(compNum))

print(cmath.cosh(compNum))
