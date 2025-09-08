from products import Product


class Store:
    def __init__(self, name):
        """ Initialize a product """
        self.name = name

    def add_product(self, product):
        """ Add a product to the store """
        pass

    def remove_product(self, product):
        """ Remove a product from the store """
        pass

    def get_total_quantity(self) -> int:
        """ Return the total quantity of the product in the store """
        pass

    def get_all_products(self) -> list[Product]:
        """ Return a list of all products in the store """
        pass

    def order(self, shopping_list) -> float:
        """ Order the product in the store """
        pass


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))