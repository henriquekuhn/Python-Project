from collections import Counter
import re

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_less_than(n):
    return [x for x in range(2, n) if is_prime(x)]

# Exemplo de uso
print(primes_less_than(10))  # Output: [2, 3, 5, 7]
print([x for x in range(2, 10) if x>4])

numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x ** 2, numeros)
print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]

import re

text = " um dois três quatro " 
print(text.split())
print(text)
print(text.strip()) # remove string
print(re.findall('o', text))
print(Counter(re.findall('o', text)))

