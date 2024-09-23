'''
Análise do Valor Limite
Teste nos valores limite 18 e 99, além dos valores imediatamente abaixo e acima desses limites.
'''

from main import test_studies

def limit_test():
    test = test_studies()

    # Valid values test: lower limit
    assert test.valida_idade(18) == "Idade válida."

    # Valid values test: higher limit
    assert test.valida_idade(99) == "Idade válida."

    # Invalid values test: lower limit
    assert test.valida_idade(17) == "Idade inválida: fora do intervalo permitido."

    # Invalid values test: higher limit
    assert test.valida_idade(100) == "Idade inválida: fora do intervalo permitido."


if __name__ == '__main__':
    limit_test()