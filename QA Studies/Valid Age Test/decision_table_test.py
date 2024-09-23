'''
Tabelas de Decisão
Crie uma tabela que abrange diferentes combinações de entradas (tipos de dados e faixas de valores) 
e as respectivas saídas.
'''

from main import test_studies

def decision_table():
    test = test_studies()


    # Valid values test: 
    assert test.valida_idade(30) == "Idade válida."

    # Invalid values test: lower value
    assert test.valida_idade(10) == "Idade inválida: fora do intervalo permitido."

    # Invalid values test: higher value
    assert test.valida_idade(120) == "Idade inválida: fora do intervalo permitido."

    # Invalid values test: non numeric
    assert test.valida_idade("trinta") == "Idade inválida: deve ser um número inteiro."

if __name__ == '__main__':
    decision_table()