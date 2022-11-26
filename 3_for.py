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



# def item_sum(items_sold):
#   result = 0
#   for amount in items_sold:
#       result += amount
#   return result


def sum_sold():
 
  for item in stock:

    name = item['product']
    total = sum(item['items_sold'])
    print(f'Суммарное количество продаж {name}: {total}')





def average_sold():
  result = 0
  i = 0
  avg = 0
  while i < 3:
    for amount in stock[i]['items_sold']:
      result += amount
      avg = result / len(stock[i]['items_sold'])
      name = stock[i]['product']
    i += 1
    result = 0
    print(f'Среднее количество продаж {name}: {avg}')
    
average_sold()

def all_sum():
  result = 0
  i = 0
  while i < 3:
    for amount in stock[i]['items_sold']:
      result += amount
    i += 1
  return f'Суммарное количество продаж всех товаров: {result}'


def all_avg():
  result = 0
  i = 0
  while i < 3:
    for amount in stock[i]['items_sold']:
      result += amount
      avg = result / len(stock[i]['items_sold'])
    i += 1
  return f'Среднее количество продаж всех товаров: {avg}'
    

def main():
  sum_sold()
 

  all_sum_sold = all_sum()
  print(all_sum_sold)
  
  all_average =  all_avg()
  print(all_average)


    
if __name__ == "__main__":
    main()
