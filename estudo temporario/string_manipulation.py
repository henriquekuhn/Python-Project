import re
from collections import Counter

# Exemplo de manipulação de strings
text = " um dois três quatro "

# Separar a string em uma lista de palavras
print("Split by spaces:", text.split())  # Output: ['um', 'dois', 'três', 'quatro']

# Exibir a string original com espaços
print("Original string:", text)  # Output: " um dois três quatro "

# Remover espaços em branco no início e no fim da string
print("Trimmed string:", text.strip())  # Output: "um dois três quatro"

# Encontrar todas as ocorrências de 'o'
print("Occurrences of 'o':", re.findall('o', text))  # Output: ['o', 'o', 'o']

# Contar as ocorrências de 'o'
print("Count of 'o':", Counter(re.findall('o', text)))  # Output: Counter({'o': 3})

# Reverter a string usando slicing
reversed_str = text[::-1]
print("Reversed string:", reversed_str)  # Output: "ortauq sêrt soid mu "

# Substituir uma substring condicionalmente
if "três" in text:
    text = text.replace("três", "tres")
print("Conditional replace:", text)  # Output: " um dois tres quatro "
