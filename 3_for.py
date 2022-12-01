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


def main():
    total_sum = 0
    total_avg = 0
    sold = 0

    for item in stock:
        name = item['product']
        total = sum(item['items_sold'])
        print(f'Суммарное количество продаж {name}: {total}')

        avg  = total / len(item['items_sold'])
        print(f'Среднее количество продаж {name}: {avg}\n')

    for item in stock:
      total_sum += sum(item['items_sold'])
      sold_all = len(item["items_sold"])
      sold += sold_all
      total_avg  = total_sum / sold

    print(f'Суммарное количество продаж всех товаров: {total_sum}')
    print(f'Среднее количество продаж всех товаров: {total_avg}')


if __name__ == "__main__":
    main()
