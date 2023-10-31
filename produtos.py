from enum import Enum

# Classe para o erro de estoque insuficiente
class OutOfStockException(Exception):
    def __init__(self, product_name):
        self.product_name = product_name
        super().__init__(f"O produto {product_name} está fora de estoque.")


class NotEnoughStockException(Exception):
    def __init__(self, product_name, product_quantity):
        self.product_name = product_name
        super().__init__(f"O produto {product_name} tem apenas {product_quantity} unidades disponiveis.")


class InvalidQuantityException(Exception):
    def __init__(self):
        super().__init__(f"A quantidade é invalida.")


# Classe que representa as informações globais de qualquer produto
class Produto():
    def __init__(self, name, bar_code, price, quantity) -> None:
        self.name = name
        self.bar_code = bar_code
        self.price = price
        self.quantity = quantity

    def show_product(self):
        print(f"Nome: {self.name} | Código de Barras: {self.bar_code} | Preço: {self.price} | Quantidade: {self.quantity}")

    def decrease_quantity(self, amount):

        if type(amount) != int:
            raise InvalidQuantityException(amount)

        elif self.quantity >= amount:
            self.quantity -= amount
            
        elif self.quantity == 0:
            raise OutOfStockException(self.name)
        else:
            raise NotEnoughStockException(self.name, self.quantity)
        
    def increase_quantity(self, amount : int):
        if not type(amount) == int:
            raise InvalidQuantityException
        else:
            self.quantity += amount

# Classes específicas para cada tipo de produto com informações exclusivas para ela
class Chip(Produto):
    def __init__(self, name, bar_code, price, quantity, marca):
        super().__init__(name, bar_code, price, quantity)
        self.marca = marca


class Notebook(Produto):
    def __init__(self, name, bar_code, price, quantity, marca):
        super().__init__(name, bar_code, price, quantity)
        self.marca = marca


class Instrument(Produto):
    def __init__(self, name, bar_code, price, quantity, marca):
        super().__init__(name, bar_code, price, quantity)
        self.marca = marca

# Representa as marcas para cada um dos produtos 
class MarcaChip(Enum):
    INTEL = 1   
    AMD = 2


class MarcaNotebook(Enum):
    MACBOOK = 1
    SAMSUNG = 2


class MarcaInstrument(Enum):
    GUITAR = 1
    BASS = 2
