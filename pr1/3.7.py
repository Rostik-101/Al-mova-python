f = 20; p30 = 9.86; n20 = 11.22; nas10 = 13.06; dod = 17.89
num = float(input('Введіть кількість споживаних кубометрів: '))
if num <= 30:
    men30 = num * p30 + f
    print('Ваш рахунок: {:.2f}'.format(men30))
elif num >= 31 <= 50:
    perep = (num - 30) * n20
    vid30_50 = 30 * p30 + perep + f
    print('Ваш рахунок: {:.2f}'.format(vid30_50))
elif num >= 51 <= 60:
    perep2 = (num - 50) * nas10
    vid50_60 = 30 * p30 + 224.4 + perep2 + f
    print('Ваш рахунок: {:.2f}'.format(vid50_60))
elif num >= 61:
    perep3 = (num - 60) * dod
    vid60 = 295.8 + 224.4 + 130.6 + perep3 + f
    print('Ваш рахунок: {:.2f}'.format(perep3))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)
