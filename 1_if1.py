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

def main(user_age):

    if user_age < 3:
      print('Relax')
      
    if user_age >= 3 and user_age < 7:
      print('You should be in kindergarten!')
    elif user_age >= 7 and user_age <= 17:
      print('You should be in school!')
    elif user_age > 17 and user_age <= 25:
      print('You should be in university!')
    elif user_age > 25:
      print('Back to work!')

if __name__ == "__main__":
    main(user_age)
