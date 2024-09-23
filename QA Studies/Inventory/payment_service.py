class PaymentService:
    def process_payment(self, amount):
        # Simula processamento de pagamento
        if amount > 0:
            return "Pagamento aprovado"
        return "Pagamento falhou"