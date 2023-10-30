

class Produto():
    def __init__(self, name, bar_code, price, quantity) -> None:
        self.name = name
        self.bar_code = bar_code
        self.price = price
        self.quantity = quantity

    def show_info(self):
        ...

    def decrease_quantity(self, amount):
        ...
    
class Chip(Produto):
    def __init__(self, name, price, quantity,bar_code) -> None:
        super().__init__(name, price, quantity,bar_code)

class Notebook(Produto):
    def __init__(self, name, price, quantity,bar_code) -> None:
        super().__init__(name, price, quantity,bar_code)

class Instrument(Produto):
    def __init__(self, name, price, quantity,bar_code) -> None:
        super().__init__(name, price, quantity,bar_code)

class Inventario():
    def __init__(self) -> None:
        self.products = []
    
    def add_to_inventory(self,product):
        self.products.append(product)
    def check_products_inventory(self):
        for product in self.products:
            print(product.name)
    def check_barcode_inventory(self):
        for product in self.products:
            print(product.bar_code)

  

a = Chip('chip','12','34','anfian#cms')
b = Instrument('piano','12','3','adf2f#cms')
inv = Inventario()
inv.add_to_inventory(a)
inv.add_to_inventory(b)
inv.check_products_inventory()

    
    