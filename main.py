import products

def main():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    print(bose.__dict__)
    print(mac.__dict__)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()

