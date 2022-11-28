"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 
      'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 
      'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 
      'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""



stock =  [
    {'product': 'iPhone 12', 
      'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 
      'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 
      'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def sum_sold():
  for item in stock:

    name = item['product']
    total = sum(item['items_sold'])
    print(f'Суммарное количество продаж {name}: {total}')


def average_sold():
  for item in stock:

    name = item['product']
    total = sum(item['items_sold'])
    avg  = total / len(item['items_sold'])
    print(f'Среднее количество продаж {name}: {avg}')


def all_sum():
  total_sum = 0
  
  for item in stock:
    total_sum += sum(item['items_sold'])

  print(f'Суммарное количество продаж: {total_sum}')


def all_avg():
  total_avg = 0
  total_sum = 0

  for item in stock:
    total_sum += sum(item['items_sold'])
    total_avg  = total_sum / len(item['items_sold'])

  print(f'Среднее количество продаж всех товаров: {total_avg}') 
    


def main():
  sum_sold()
 
  average_sold()

  all_sum()

  all_avg()
    
if __name__ == "__main__":
    main()
