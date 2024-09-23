'''
Regras:
Valor da compra:

Deve ser maior que 0.
Se for inferior a R$10,00, retorna "Erro: valor mínimo para compra é R$10,00".
Se for superior a R$10.000,00, retorna "Erro: valor máximo para compra é R$10.000,00".
Método de pagamento:

Para "cartão de crédito", deve ser permitido parcelar em até 12 vezes.
Para "boleto" e "pix", o número de parcelas deve ser ignorado.
Parcelamento:

O número de parcelas deve ser entre 1 e 12 para "cartão de crédito".
Se o número de parcelas for maior que 12 ou menor que 1, retorna "Erro: número de parcelas inválido".
Sucesso:

Se tudo estiver correto, o sistema retorna "Pagamento aprovado".
'''

from main import payment

def equivalence_class():
    test = payment()

    # Invalid values
    assert test.processar_pagamento(0, "cartão de crédito", 1) == "Erro: valor da compra deve ser maior que zero."
    assert test.processar_pagamento(-1, "cartao de credito", 1) == "Erro: valor da compra deve ser maior que zero."
    assert test.processar_pagamento(9.99, "cartao de credito", 1) == "Erro: valor mínimo para compra é R$10,00."
    assert test.processar_pagamento(10000.01, "cartao de credito", 1) == "Erro: valor máximo para compra é R$10.000,00."

    # Invalid method
    assert test.processar_pagamento(100, "metodo", 1) == "Erro: método de pagamento inválido."

    # Invalid installments
    assert test.processar_pagamento(100, "cartão de crédito", 0) == "Erro: número de parcelas inválido."
    assert test.processar_pagamento(100, "cartão de crédito", 13) == "Erro: número de parcelas inválido."

    # Valid values
    assert test.processar_pagamento(100, "cartão de crédito", 12) == "Pagamento aprovado" 
    assert test.processar_pagamento(100, "cartão de crédito", 1) == "Pagamento aprovado"  

    assert test.processar_pagamento(100, "pix", 13) == "Pagamento aprovado"   
    assert test.processar_pagamento(100, "boleto", 13) == "Pagamento aprovado"
    assert test.processar_pagamento(100, "pix") == "Pagamento aprovado"   
    assert test.processar_pagamento(100, "boleto") == "Pagamento aprovado" 

if __name__ == '__main__':
    equivalence_class()