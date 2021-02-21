a = int(input('Введи ціле число а: '))
b = int(input('Введи ціле число b: '))
c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = b / a
print(f)
g = b // a
print(g)
h = a // b
print(h)
i = b ** a
print(i)

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)