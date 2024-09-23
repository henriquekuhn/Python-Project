class OrderRepository:
    def save_order(self, order):
        # Simula salvamento do pedido
        if 'id' not in order:
            raise ValueError("Pedido inválido: ID ausente")
        return f"Pedido {order['id']} salvo com sucesso"