year = int(input('Введіть рік: '))

if year % 400 == 0:
    print("%d Високосний" %year)
elif year % 100 == 0:
    print("%d НЕ високосний" %year)
elif year % 4 == 0:
    print("%d високосний" %year)
else:
    print("%d НЕ високосный" %year)

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)