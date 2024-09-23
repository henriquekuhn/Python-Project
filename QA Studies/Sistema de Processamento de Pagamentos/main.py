class payment:
    def processar_pagamento(self, valor_compra: float, metodo_pagamento: str, numero_parcelas: int = 1) -> str:
        # Validação do valor da compra
        if valor_compra <= 0:
            return "Erro: valor da compra deve ser maior que zero."
        if valor_compra < 10:
            return "Erro: valor mínimo para compra é R$10,00."
        if valor_compra > 10000:
            return "Erro: valor máximo para compra é R$10.000,00."

        # Validação do método de pagamento
        if metodo_pagamento == "cartão de crédito":
            # Verifica se o número de parcelas é válido para cartão de crédito
            if not (1 <= numero_parcelas <= 12):
                return "Erro: número de parcelas inválido."
        elif metodo_pagamento in ["boleto", "pix"]:
            # Para boleto e pix, o número de parcelas não deve afetar o resultado
            numero_parcelas = 1  # Ignora o número de parcelas
        else:
            return "Erro: método de pagamento inválido."

        return "Pagamento aprovado"
