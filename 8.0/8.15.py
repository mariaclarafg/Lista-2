class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_data(self):
        print(f"Product Name: {self.name}\nPrice: ${self.price}\nQuantity in Stock: {self.quantity}")

class ImportedProduct(Product):
    def __init__(self, name, price, quantity, tax):
        super().__init__(name, price, quantity)
        self.tax = tax

    def final_price(self):
        final_price = self.price + (self.price * self.tax / 100)
        print(f"Final Price: ${final_price:.2f}")

imported_product = ImportedProduct("Book", 500, 10, 10)
imported_product.show_data()
imported_product.final_price()
