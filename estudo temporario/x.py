import re

def analyze_text(text):
    # 1. Contagem de Palavras e Caracteres
    text_list = text.split()
    print(len(text_list))
    letras = [c for n in range(len(text_list)) for c in text_list[n]]
    print(len(letras))
    print(re.sub("Python", "Java", text))
    int_numbers = map(int, re.findall("\d+", text))
    print(sum(int_numbers))
    palindromo = [word for word in text_list if word == word[::-1]]
    print(palindromo)
    print(text[::-1])
    reversed_words = ' '.join(w[::-1] for w in text_list)
    print(reversed_words)



# Exemplo de uso
text = "Python é uma linguagem que é muito interessante. O número 123 é um exemplo de número, e 121 é um palíndromo."
analyze_text(text)