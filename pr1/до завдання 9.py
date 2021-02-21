R = 8.314
P = float(input('Введіть тиск у паскалях: '))
V = float(input('Введіть обєм: '))
T = float(input('Введіть температуру у Цельсіях: '))
K = T + 273.15
n = (P * V) / (K * R)
print('Молярна маса газу: {:.2f}'.format(n))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)
