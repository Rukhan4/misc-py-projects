"""
Product Inventory Project - Create an application which manages
an inventory of products. Create a product class which has a
price, id, and quantity on hand. Then create an inventory class
which keeps track of various products and can sum up the inventory
value.
"""


class Product():
    def __init__(self, price, pid, qty):
        """class constructor

        Args:
            price ([float]): [price of the product]
            pid ([int]): [product ID number]
            qty ([int]): [quantity of product]
        """
        self.price = price
        self.pid = pid
        self.qty = qty

    def update_qty(self, qty, method="add"):
        """[Updates the quantity of products. By default, adds the passed quantity.
        Pass method as subtract to subtract the quantity]

        Args:
            method (str, optional): Defaults to "add".
        """
        if method == "add":
            self.qty += qty
        elif method == "subtract":
            self.qty = max(0, self.qty-qty)


class Inventory():
    def __init__(self):
        """
        initialize the class instance
        """
        self.products = []  # list to hold all the products

    def add(self, product):
        """
        Adds a passed Product to the list of products.
        """
        self.products.append(product)

    def print_inventory(self):
        """
        Prints the current inventory, and the total value
        of products.
        """
        value = 0
        for product in self.products:
            print("%d\t%s\t%.02f each" % (product.pid, product.qty, product.price))
            value += (product.price*product.qty)
            print(f'Total value={round(value, 2)}')


if __name__ == "__main__":
    p1 = Product(1.4, 123, 50)
    p2 = Product(225.50, 3432, 100)
    p3 = Product(100.40, 754, 80)

    i = Inventory()
    i.add(p1)
    i.add(p2)
    i.add(p3)
    i.print_inventory()

    p1.update_qty(10)
    i.print_inventory()

    p1.update_qty(10, method="subtract")
    i.print_inventory
