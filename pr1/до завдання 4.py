tip = 14
tax = 18
dish = input('Назва страви: ')
portions = int(input('Кількість порцій: '))
price = float(input('Ціна за порцію: '))
podatok = (price * portions * tax) / 100
chayovi = (price * portions * tip) / 100
suma = price * portions + podatok + chayovi
print('Податок до страви: {:.2f}'.format(podatok))
print('Чайові: {:.2f}'.format(chayovi))
print('Загальна сума до сплати: {:.2f}'.format(suma))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)
