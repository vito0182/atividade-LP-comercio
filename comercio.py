

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
    
class Book(Produto):
    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)

class Notebook(Produto):
    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)

class Instrument(Produto):
    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)


