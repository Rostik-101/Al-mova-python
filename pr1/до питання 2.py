c = float(input('°C: '))
f = (c * 9/5) + 32
k = c + 273.15
print('''°F: {}
°K: {}'''.format(f, k))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)


