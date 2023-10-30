from enum import Enum

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

# Classe que representa as informações globais de qualquer produto
class Produto():
    def __init__(self, name, bar_code, price, quantity) -> None:
        self.name = name
        self.bar_code = bar_code
        self.price = price
        self.quantity = quantity

    def show_product(self):
        print(f"Nome: {self.name}, Código de Barras: {self.bar_code}, Preço: {self.price}, Quantidade: {self.quantity}")

    def decrease(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            return False # MUDAR ISSO PRA RAISE!

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

# Classe para gerenciar o inventário
class Inventario():
    def __init__(self):
        self.products = []
    
    # adiciona o produto dentro do inventário.
    def add_to_inventory(self, product):
        self.products.append(product)
    
    # Mostra todos os produtos que pertencem ao inventário
    def check_products_inventory(self):
        print("Produtos no inventário:")
        for product in self.products:
            product.show_product()
            
    # Vê se o código de barras dado está associado a algum produto registrado
    def check_barcode_inventory(self, bar_code):
        for product in self.products:
            if product.bar_code == bar_code:
                return product

    def sell_product(self, bar_code, amount):
        product = self.check_barcode_inventory(bar_code)
        product.decrease(amount)
        print(f"Venda de {amount} unidades de {product.name}.")
        # ADD EXCECAO PROPRIA

# Exemplo:
a = Chip('Intel Z790', '12345', 12.0, 34, MarcaChip.INTEL)
b = Notebook('MacBook', '54321', 1200.0, 3, MarcaNotebook.MACBOOK)
c = Instrument('Guitarra', '67890', 500.0, 67, MarcaInstrument.GUITAR)
inv = Inventario()
inv.add_to_inventory(a)
inv.add_to_inventory(b)
inv.add_to_inventory(c)
inv.sell_product('12345', 1)  
inv.check_products_inventory()