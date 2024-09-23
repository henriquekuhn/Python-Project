import unittest
from unittest.mock import MagicMock
from inventory_service import InventoryService
from payment_service import PaymentService
from order_repository import OrderRepository
from order_service import OrderService

class TestOrderService(unittest.TestCase):

    def setUp(self):
        self.inventory_service = MagicMock(spec=InventoryService)
        self.payment_service = MagicMock(spec=PaymentService)
        self.order_repository = MagicMock(spec=OrderRepository)
        self.order_service = OrderService(
            self.inventory_service,
            self.payment_service,
            self.order_repository
        )

    def test_estoque_insuficiente(self):
        self.inventory_service.check_stock.side_effect = ValueError("Estoque insuficiente para processar o pedido")
        result = self.order_service.process_order("item1", 15, 100)
        self.assertEqual(result, "Estoque insuficiente para processar o pedido")

    def test_pagamento_falhou(self):
        self.inventory_service.check_stock.return_value = True
        self.payment_service.process_payment.return_value = "Pagamento falhou"
        result = self.order_service.process_order("item1", 5, 100)
        self.assertEqual(result, "Erro no processamento do pagamento")

    def test_pedido_invalido(self):
        self.inventory_service.check_stock.return_value = True
        self.payment_service.process_payment.return_value = "Pagamento aprovado"
        self.order_repository.save_order.side_effect = ValueError("Pedido inválido: ID ausente")
        result = self.order_service.process_order("item1", 5, 100)
        self.assertEqual(result, "Pedido inválido: ID ausente")

    def test_pedido_processado_com_sucesso(self):
        self.inventory_service.check_stock.return_value = True
        self.payment_service.process_payment.return_value = "Pagamento aprovado"
        self.order_repository.save_order.return_value = "Pedido order123 salvo com sucesso"
        result = self.order_service.process_order("item1", 5, 100)
        self.assertEqual(result, "Pedido order123 salvo com sucesso")

if __name__ == '__main__':
    unittest.main()
