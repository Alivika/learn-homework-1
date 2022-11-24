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

def main(one, two):
  if not isinstance(one, str) or not isinstance(two, str):
      print(0)

  if isinstance(one, str) and isinstance(one, str):
      if one == two:
        print(1)
      elif one != two and len(one) > len(two):
        print(2)
      elif one != two and two == 'learn':
        print(3)


if __name__ == "__main__":
    main(3, 1)

if __name__ == "__main__":
    main(3, '1')

if __name__ == "__main__":
    main('3', '1')

if __name__ == "__main__":
    main('Cloud', 'Sun')

if __name__ == "__main__":
    main('3', 'learn')

if __name__ == "__main__":
    main('3', '3')
