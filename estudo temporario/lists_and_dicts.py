# Exemplo de manipulação de listas e dicionários

# Lista
numbers = [1, 2, 3, 4, 5]

# Adicionar um elemento à lista
numbers.append(10)
print("List after append:", numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Remover um elemento da lista
numbers.remove(10)
print("List after remove:", numbers)  # Output: [1, 2, 4, 5, 6]

# List comprehension para criar uma nova lista com quadrados dos números
squares = [x ** 2 for x in numbers]
print("List comprehension (squares):", squares)  # Output: [1, 4, 16, 25, 36]

# Dicionário
person = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}

# Adicionar um novo item ao dicionário
person["email"] = "alice@example.com"
print("Dictionary after adding email:", person)

# Atualizar um valor existente
person["age"] = 31
print("Dictionary after updating age:", person)

# Dict comprehension para criar um dicionário com números e seus quadrados
number_squares = {x: x ** 2 for x in numbers}
print("Dict comprehension (number squares):", number_squares)  # Output: {1: 1, 2: 4, 4: 16, 5: 25, 6: 36}
