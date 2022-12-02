"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def check_str(one, two):
  if not isinstance(one, str) or not isinstance(two, str):
    return 0

  if one == two:
    return 1

  if one != two and len(one) > len(two):
    return 2

  if one != two and two == 'learn':
    return 3


def main():
    print(check_str(3, 1))
    print(check_str(3, '1'))
    print(check_str('Cloud', 'Sun'))
    print(check_str('3', 'learn'))
    print(check_str('hi', 'hi'))


if __name__ == "__main__":
    main()
