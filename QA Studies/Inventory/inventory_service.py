class InventoryService:
    def check_stock(self, item, quantity):
        # Simula checagem de estoque
        stock = {'item1': 10, 'item2': 0}
        if item not in stock:
            raise ValueError("Item não encontrado no estoque")
        if stock[item] < quantity:
            raise ValueError("Estoque insuficiente para processar o pedido")
        return True