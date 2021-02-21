height = float(input('Введи свій зріст в см: '))
inch = height / 2.54
futi = height / 30.48
print('''Ваш зріст в дюймах: {}
Ваш зріст в футах: {}'''.format(inch, futi))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)