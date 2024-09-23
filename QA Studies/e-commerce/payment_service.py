# payment_service.py
from payment_gateway import PaymentGateway
from repository import PaymentRepository

class PaymentService:
    def __init__(self):
        self.gateway = PaymentGateway()
        self.repository = PaymentRepository()

    def process_payment(self, valor_compra: float, metodo_pagamento: str, numero_parcelas: int = 1) -> str:
        resultado = self.gateway.realizar_pagamento(valor_compra, metodo_pagamento, numero_parcelas)
        if resultado == "Pagamento realizado":
            # Simular o salvamento da transação
            self.repository.salvar_transacao(valor_compra, metodo_pagamento, numero_parcelas)
            return "Pagamento aprovado"
        return resultado
