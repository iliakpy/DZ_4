def ask_year():
    year = input('Ввведите год рождения А.С.Пушкина:')
    while year != '1799':
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина:')


def ask_day():
    day = input('Ввведите день рождения Пушкин?')
    while day != '6':
        print("Не верно")
        day = input('Ввведите день рождения Пушкин?')



ask_day()
ask_year()
ask_day()
ask_year()

print('Верно')
