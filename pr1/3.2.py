print('''Ваше місце проживання:
1)Будинок
2)Квартира
3)Гуртожиток''')
number = int(input('Номер: '))
t = int(input('Скільки годин ви дома? '))
if number == 1:
    if t > 18:
     print("Наша рекомендована тваринка - в'єтнамське порося")
    if t >= 10 < 17:
        print('Наша рекомендована тваринка - собака')
    if t < 10:
        print('Наша рекомендована тваринка - змія')
if number == 2:
    if t >= 10:
        print('Наша рекомендована тваринка - кішка')
    if t < 10:
        print("Наша рекомендована тваринка - хом'як")
if number == 3:
    if t >= 6:
        print('Наша рекомендована тваринка - рибки')
    if t < 6:
        print('Наша рекомендована тваринка - мурашник')

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)



