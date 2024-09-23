# Classe válida: valores entre 18 e 99.
# Classe inválida: valores abaixo de 18 e acima de 99.

from main import test_studies

def test_particao_por_classes():
    
    # Instância da classe
    test = test_studies()

    # Valid values test: valores entre 18 e 99.
    assert test.valida_idade(25) == "Idade válida.", "Erro: valor dentro da classe válida falhou."

    # Invalid lower values test: valores abaixo de 18
    assert test.valida_idade(10) == "Idade inválida: fora do intervalo permitido.", "Erro: valor abaixo da classe válida falhou."

    # Invalid higher values test: valores acima de 99
    assert test.valida_idade(120) == "Idade inválida: fora do intervalo permitido.", "Erro: valor acima da classe válida falhou."

if __name__ == '__main__':
    test_particao_por_classes()
