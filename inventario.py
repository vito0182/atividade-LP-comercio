from produtos import OutOfStockException, NotEnoughStockException, InvalidQuantityException

# Classe para gerenciar o inventário
class Inventario():
    def __init__(self):
        self.products = []
    
    # adiciona o produto dentro do inventário.
    def add_to_inventory(self, product):
        self.products.append(product)
    
    # Mostra todos os produtos que pertencem ao inventário
    def check_products_inventory(self):
        print("----- Produtos no inventário -----\n")
        for product in self.products:
            product.show_product()
            
    # Vê se o código de barras dado está associado a algum produto registrado
    def check_barcode_inventory(self, bar_code):
        for product in self.products:
            if product.bar_code == bar_code:
                return product

    def sell_product(self, bar_code, amount):
        product = self.check_barcode_inventory(bar_code)
        try:
            product.decrease_quantity(amount)
            print(f"Venda de {amount} unidades de {product.name}.")
        except OutOfStockException as e:
            print(f"Erro ao vender: {e}")
        except NotEnoughStockException as e:
            print(f"Erro ao vender: {e}")

    def add_product(self, bar_code, amount):
        product = self.check_barcode_inventory(bar_code)
        try:
            product.increase_quantity(amount)
            print(f"Aumento de {amount} unidades de {product.name} no estoque.")
        except InvalidQuantityException as e:
            print(f"Erro ao adicionar ao estoque: {e}")