import json

import math
from datetime import datetime

from app.car import Car
from app.shop import Shops


class Customer:
    def __init__(self,
                 name: str,
                 products_cart: dict,
                 customer_location: list[int],
                 money: int,
                 car: Car
                 ) -> None:
        self.name = name
        self.products_cart = products_cart
        self.customer_location = customer_location
        self.money = money
        self.car = car

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance(self, shop_location: list, fuel_price: float, fuel_consumption: float):
        x1, y1 = self.customer_location
        x2, y2 = shop_location
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        price_road = dist / 100 * fuel_consumption * fuel_price * 2
        return round(price_road, 2)

    def shopping_time(self, shop: Shops) -> None:
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Data: {current_time}")
        print(f"Thanks, {self.name}, for your purchase!")
        print(f"You have bought:")

        total_cost = 0
        for product, quantity in self.products_cart.items():
            if product in shop.products:
                cost_product = shop.products[product] * quantity
                print(f"{quantity} {product}s for {cost_product} dollars")
                total_cost += (int(cost_product)
                               if cost_product == int(cost_product)
                               else cost_product)

        print(f"Total cost is {round(total_cost, 2)} dollars\n"f"See you again!")
