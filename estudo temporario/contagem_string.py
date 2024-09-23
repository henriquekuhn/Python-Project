import re
from collections import Counter

def contar_palavras(texto):
    # Removendo pontuações e convertendo para minúsculas
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower())
    # Separando as palavras
    palavras = texto_limpo.split()
    # Lista de palavras comuns a serem ignoradas
    palavras_comuns = {'de', 'a', 'o', 'e', 'é', 'em', 'um', 'uma', 'do', 'da', 'das', 'dos'}

    # Filtrando as palavras
    palavras_filtradas = [palavra for palavra in palavras if palavra not in palavras_comuns]
    # Contando a ocorrência das palavras
    contagem = Counter(palavras_filtradas)

    contagem_palavras = {}
    for palavra in palavras:
        # Ignora palavras comuns
        if palavra not in palavras_comuns:
            # Incrementa a contagem da palavra no dicionário
            if palavra in contagem_palavras:
                contagem_palavras[palavra] += 1
            else:
                contagem_palavras[palavra] = 1
    return dict(contagem)

# Teste
texto = "Python é uma linguagem de programação poderosa e versátil. Python é popular em ciência de dados."
resultado = contar_palavras(texto)
print(resultado)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# String original
sentence = "hello world"
# Dividindo a string em palavras
words = sentence.split()  # ['hello', 'world']
# Invertendo a ordem das palavras
reversed_words = words[::-1]  # ['world', 'hello']
# Juntando as palavras em uma nova string
reversed_sentence = ' '.join(reversed_words)
print(reversed_sentence)  # Output: "world hello"

# Inverter a string usando slicing
reversed_str = sentence[::-1]
# Exibir a string invertida
print("Reversed string:", reversed_str)  # Output: "dlroW olleH"