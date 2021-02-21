t1 = 0.05; t2 = 0.04; t3 = 0.02
g1 = 20; g2 = 35; g3 = 85

tarif = float(input('''Ваш тариф?
1) Тариф 1000
2) Тариф 2000
3) Тариф 3000\n'''))
mb = float(input('Кількість використаних МБ: '))

if tarif == 1 and mb < 1000:
    print('До сплати 20 грн.\nПри переході на більш дорогий тариф ви платили 35 грн(Тариф 2000) і 85 грн(Тариф 5000)')
elif tarif == 1 and mb > 1000:
    splata1 = (mb - 1000) * t1 + g1
    print('До сплати {} грн'.format(splata1))
    if mb < 2000:
        print('Якби у вас був Тариф 2000 ви б заплатили - 35грн\nЯкби у вас був Тариф 5000 ви б заплатили - 85грн')
    elif 2000 < mb < 5000:
        perehod2 = (mb - 2000) * t2 + g2
        print('Якби у вас був тариф 2000 ви б заплатили - {} грн\nЯкби у вас був Тариф 5000 ви б заплатили 85 грн'.format(perehod2))
    elif mb > 5000:
        perehod3 = (mb - 5000) * t3 + g3
        print('Якби у вас був тариф 5000 ви б заплатили - {} грн'.format(perehod3))


if tarif == 2 and mb < 2000:
    print('До сплати 35 грн.\nПри переході на більш дорогий тариф ви платили 85 грн(Тариф 5000)')
elif tarif == 2 and mb > 2000:
    splata2 = (mb - 2000) * t2 + g2
    print('До сплати {} грн'.format(splata2))
    if mb < 5000:
        print('Якби у вас був Тариф 5000 ви б заплатили - 85 грн.')
    elif mb > 5000:
        perehod3 = (mb - 5000) * t3 + g3
        print('Якби у вас був Тариф 5000 ви б заплатили - {} грн'.format(perehod3))

if tarif == 3 and mb < 5000:
    print('До сплати 85 грн.')
elif tarif == 3 and mb > 5000:
    splata3 = (mb - 5000) * t3 + g3
    print('До сплати {} грн'.format(splata3))

name = "Козачков Ростислав"
import datetime
print('Автор програми: ' + name)
a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)