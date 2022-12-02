"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

user_age = int(input('Insert your age: '))


def age_res(user_age):

    if user_age < 3:
      return 'Relax'
      
    if user_age >= 3 and user_age < 7:
      return 'You should be in kindergarten!'

    if user_age >= 7 and user_age <= 17:
      return 'You should be in school!'

    if user_age > 17 and user_age <= 25:
      return 'You should be in university!'

    if user_age > 25:
      return 'Back to work!'


def main():
  print(age_res(user_age))


if __name__ == "__main__":
    main()
