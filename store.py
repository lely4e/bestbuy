import products


class Store:
    def __init__(self, products_list):
        """ Initialize a product """
        self.products = products_list

    def add_product(self, product):
        """ Add a product to the store """
        self.products.append(product)

    def remove_product(self, product):
        """ Remove a product from the store """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """ Return the total quantity of the product in the store """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """ Return a list of all products in the store """
        return self.products

    def order(self, shopping_list) -> float:
        """ Order the product in the store """
        # Gets a list of tuples, where each tuple has 2 items:
        # Product (Product class) and quantity (int)
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


def main():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    product_items = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(product_items[0], 1), (product_items[1], 2)]))


if __name__ == "__main__":
    main()
