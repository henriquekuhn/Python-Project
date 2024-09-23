import re

def advanced_string_manipulation():
    # Concatenar Strings
    str1 = "Hello"
    str2 = "World"
    result = str1 + " " + str2
    print("Concatenation:", result)  # Output: "Hello World"
    
    # Repetir Strings
    repeated_str = str1 * 3
    print("Repetition:", repeated_str)  # Output: "HelloHelloHello"
    
    # Acessar Caracteres
    first_char = str1[0]
    last_char = str1[-1]
    print("First character:", first_char)  # Output: "H"
    print("Last character:", last_char)    # Output: "o"
    
    # Fatiamento de Strings
    substring = str1[0:4]
    print("Substring:", substring)  # Output: "Hell"
    
    # Converter para Maiúsculas e Minúsculas
    upper_str = str1.upper()
    lower_str = str2.lower()
    print("Uppercase:", upper_str)  # Output: "HELLO"
    print("Lowercase:", lower_str)  # Output: "world"
    
    # Remover Espaços em Branco
    str3 = "   Hello World   "
    trimmed_str = str3.strip()
    print("Trimmed string:", trimmed_str)  # Output: "Hello World"
    
    # Substituir Substrings
    new_str = result.replace("World", "Python")
    print("Replaced string:", new_str)  # Output: "Hello Python"
    
    # Dividir uma String em uma Lista
    str4 = "Hello World Python"
    word_list = str4.split()
    print("Split by spaces:", word_list)  # Output: ['Hello', 'World', 'Python']
    
    str5 = "apple,banana,orange"
    fruit_list = str5.split(',')
    print("Split by comma:", fruit_list)  # Output: ['apple', 'banana', 'orange']
    
    # Juntar uma Lista em uma String
    joined_str = ' '.join(word_list)
    print("Joined list:", joined_str)  # Output: "Hello World Python"
    
    # Verificar Presença de Substring
    is_present = "World" in result
    print("Is 'World' present?:", is_present)  # Output: True
    
    is_not_present = "Python" not in result
    print("Is 'Python' not present?:", is_not_present)  # Output: True
    
    # Formatar Strings
    name = "John"
    age = 30
    formatted_str = f"My name is {name} and I am {age} years old."
    print("Formatted string (f-string):", formatted_str)  # Output: "My name is John and I am 30 years old."
    
    formatted_str2 = "My name is {} and I am {} years old.".format(name, age)
    print("Formatted string (format()):", formatted_str2)  # Output: "My name is John and I am 30 years old."
    
    # Encontrar Substring
    index = result.find("World")
    print("Index of 'World':", index)  # Output: 6
    
    index_not_found = result.find("Python")
    print("Index of 'Python':", index_not_found)  # Output: -1
    
    # Contar Ocorrências de uma Substring
    str6 = "banana"
    count_a = str6.count("a")
    print("Count of 'a' in 'banana':", count_a)  # Output: 3
    
    # Inverter uma String
    reversed_str = result[::-1]
    print("Reversed string:", reversed_str)  # Output: "dlroW olleH"
    
    # Substituir uma Substring Condicionalmente
    if "World" in result:
        result = result.replace("World", "Python")
    print("Conditional replace:", result)  # Output: "Hello Python"

    print(result.split()[1] + " " + result.split()[0])

advanced_string_manipulation()
