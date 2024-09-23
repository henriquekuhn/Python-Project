'''
Grafos de Causa e Efeito
Mapeie os possíveis valores de entrada (causas) e o resultado correspondente (efeito). Teste os casos derivados.
'''

from main import test_studies

def cause_effect():
    test = test_studies()

    # Causa: idade dentro do intervalo -> Efeito: idade válida
    assert test.valida_idade(45) == "Idade válida."

    # Causa: idade fora do intervalo (menor) -> Efeito: idade inválida
    assert test.valida_idade(12) == "Idade inválida: fora do intervalo permitido."

    # Causa: valor não numérico -> Efeito: mensagem de erro de tipo
    assert test.valida_idade("trinta") == "Idade inválida: deve ser um número inteiro."

if __name__ == '__main__':
    cause_effect()
