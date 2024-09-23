class OrderService:
    def __init__(self, inventory_service, payment_service, order_repository):
        self.inventory_service = inventory_service
        self.payment_service = payment_service
        self.order_repository = order_repository

    def process_order(self, item, quantity, amount):
        try:
            self.inventory_service.check_stock(item, quantity)
            payment_status = self.payment_service.process_payment(amount)
            if payment_status != "Pagamento aprovado":
                return "Erro no processamento do pagamento"
            order = {'id': 'order123', 'item': item, 'quantity': quantity}
            return self.order_repository.save_order(order)
        except ValueError as e:
            return str(e)