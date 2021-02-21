rating = input('Введіть буквену оцінку - ')

if rating == 'A+':
    print('Ваша оцінка 4+')
elif rating == 'A':
    print('Ваша оцінка 4.0')
elif rating == 'A-':
    print('Ваша оцінка 3.7')
elif rating == 'B+':
    print('Ваша оцінка 3.3')
elif rating == 'B':
    print('Ваша оцінка 3.0')
elif rating == 'B-':
    print('Ваша оцінка 2.7')
elif rating == 'C+':
    print('Ваша оцінка 2.3')
elif rating == 'C':
    print('Ваша оцінка 2.0')
elif rating == 'C-':
    print('Ваша оцінка 1.7')
elif rating == 'D+':
    print('Ваша оцінка 1.3')
elif rating == 'D':
    print('Ваша оцінка 1.0')
elif rating == 'F':
    print('Ваша оцінка 0')
else:
    print('Такої оцінки немає!')

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)
