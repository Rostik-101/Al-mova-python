day = int(input('Введіть кількість днів: '))
hours = int(input('Введіть кількість годин: '))
minutes = int(input('Введіть кількість хвилин: '))
s = int(input('Введіть кількість секунд: '))
ms = minutes * 60
hs = hours * 60 * 60
ds = day * 24 * 60 * 60
summa = ms + hs + ds + s
print('Кількість секунд: {}'.format(summa))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)