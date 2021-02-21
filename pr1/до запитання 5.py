s1 = 75 #штучки
st1 = 112 #штукенції
s = int(input('Кількість штучок: '))
st = int(input('Кількість штукенцій: '))
mass = (s1 * s) + (st1 * st)
print('Ваша загальна маса: {} г.'.format(mass))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)