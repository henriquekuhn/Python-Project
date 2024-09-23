'''
Teste Baseado em Estados
Modele o estado do sistema (se o sistema está pronto para validar ou rejeitar). 
Aplique o teste em diferentes estados.
'''

from main import test_studies

def state_based():

    test = test_studies()
    # Estado: Sistema pronto para validar idade -> Efeito: idade válida
    assert test.valida_idade(50) == "Idade válida."

    # Estado: Sistema pronto para rejeitar idade inválida -> Efeito: idade inválida
    assert test.valida_idade(200) == "Idade inválida: fora do intervalo permitido."

    if __name__ == '__main__':
        state_based()