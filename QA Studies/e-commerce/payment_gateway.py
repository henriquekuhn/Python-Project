# payment_gateway.py
class PaymentGateway:
    def realizar_pagamento(self, valor_compra, metodo_pagamento, numero_parcelas):
        # Lógica para realizar o pagamento
        if metodo_pagamento not in ["cartão de crédito", "boleto", "pix"]:
            return "Erro: método de pagamento inválido."
        if valor_compra <= 0:
            return "Erro: valor da compra deve ser maior que zero."
        if valor_compra < 10:
            return "Erro: valor mínimo para compra é R$10,00."
        if valor_compra > 10000:
            return "Erro: valor máximo para compra é R$10.000,00."
        if metodo_pagamento == "cartão de crédito":
            if not (1 <= numero_parcelas <= 12):
                return "Erro: número de parcelas inválido."
        return "Pagamento realizado"
