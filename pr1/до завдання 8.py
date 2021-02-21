bread = 8.50
discount = 60
numbread = int(input('Введіть кількість буханок хліба: '))
cost = numbread * bread
print('Вартість товару за свіжий хліб: {:>20.2f} грн.'.format(cost))
cdis = cost * discount / 100
print('Вартість товару за вчорашній хліб: {:>17.2f} грн.'.format(cdis))
sum = cost + cdis
print('Загальна сума покупки: {:>29.2f} грн.'.format(sum))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)