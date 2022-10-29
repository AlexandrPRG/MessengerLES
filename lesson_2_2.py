import json


def write_order_to_json(item: str,
                        quantity:int,
                        price:float,
                        buyer:str,
                        date:str):
    dict_write = {'item':item,
                  'quantity':quantity,
                  'price':price,
                  'buyer':buyer,
                  'date':date,
                  }
    with open('orders.json', 'a', encoding='utf-8') as f:
        json.dump(dict_write, f, indent=4, separators=(',', ':'))


if __name__ == '__main__':
    write_order_to_json('product_1', 1, 11.1, 'buyer_1', date='21/1/11')
    write_order_to_json('product_2', 2, 22.2, 'buyer_2', date='22/2/22')
