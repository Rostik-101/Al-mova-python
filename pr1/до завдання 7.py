vnesok = float(input('Ваш внесок: '))
stavka = float(input('Ваша річна відсоткова ставка: '))
kstskl = float(input('Введіть кількість разів складання відсотку за рік: '))
years = int(input('Кількість років: '))
rstavka = stavka / 100
syears = kstskl * years
a = (rstavka / kstskl + 1)**syears * vnesok
print('Ваш дохід через {} років: {:.2f}'.format(years, a))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)