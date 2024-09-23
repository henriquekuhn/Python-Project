import unittest
from unittest.mock import MagicMock
from payment_service import PaymentService
from payment_gateway import PaymentGateway
from repository import PaymentRepository

class TestPaymentService(unittest.TestCase):

    def setUp(self):
        self.payment_service = PaymentService()
        
        # Mockar as camadas de integração e persistência
        self.payment_service.gateway = MagicMock(spec=PaymentGateway)
        self.payment_service.repository = MagicMock(spec=PaymentRepository)

    def test_valor_compra_invalido(self):
        # Configurar mocks para retornar os erros esperados
        self.payment_service.gateway.realizar_pagamento.side_effect = [
            "Erro: valor da compra deve ser maior que zero.",
            "Erro: valor mínimo para compra é R$10,00.",
            "Erro: valor máximo para compra é R$10.000,00."
        ]
        
        # Testar valores inválidos
        result = self.payment_service.process_payment(0, "cartão de crédito", 1)
        self.assertEqual(result, "Erro: valor da compra deve ser maior que zero.")
        
        result = self.payment_service.process_payment(9.99, "cartão de crédito", 1)
        self.assertEqual(result, "Erro: valor mínimo para compra é R$10,00.")
        
        result = self.payment_service.process_payment(10000.01, "cartão de crédito", 1)
        self.assertEqual(result, "Erro: valor máximo para compra é R$10.000,00.")

    def test_metodo_pagamento_invalido(self):
        # Configurar mock para retornar erro de método inválido
        self.payment_service.gateway.realizar_pagamento.return_value = "Erro: método de pagamento inválido."

        result = self.payment_service.process_payment(100, "cheque", 1)
        self.assertEqual(result, "Erro: método de pagamento inválido.")

    def test_pagamento_aprovado(self):
        # Mock da resposta do gateway de pagamento
        self.payment_service.gateway.realizar_pagamento.return_value = "Pagamento realizado"

        result = self.payment_service.process_payment(100, "cartão de crédito", 1)
        self.assertEqual(result, "Pagamento aprovado")

        # Verifica se a transação foi salva
        self.payment_service.repository.salvar_transacao.assert_called_with(100, "cartão de crédito", 1)

    def test_pagamento_falhou(self):
        # Mock de uma falha na API de pagamento
        self.payment_service.gateway.realizar_pagamento.return_value = "Erro: falha na comunicação com o gateway de pagamento."

        result = self.payment_service.process_payment(100, "cartão de crédito", 1)
        self.assertEqual(result, "Erro: falha na comunicação com o gateway de pagamento.")

        # Verifica se a transação não foi salva
        self.payment_service.repository.salvar_transacao.assert_not_called()

if __name__ == '__main__':
    unittest.main()
