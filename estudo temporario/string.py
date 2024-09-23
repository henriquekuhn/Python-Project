import re
from functools import reduce

def reverse_string_preserve_spaces(s):
    chars = [c for c in s if c != ' ']
    reversed_chars = chars[::-1]
    result = []
    char_index = 0
    for c in s:
        if c == ' ':
            result.append(' ')
        else:
            result.append(reversed_chars[char_index])
            char_index += 1
    return ''.join(result)

# Exemplo de uso
print(reverse_string_preserve_spaces("abc def"))  # Output: "fed cba"

def correct_user_register(user):
    # Padronizar nome
    user["nome_completo"] = user["nome_completo"].title()
    # Checar email
    email = user["email"]
    if not re.match(r"[a-zA-Z0-9_.]+@+[a-zA-Z0-9]+\.+[a-zA-Z]{2,}", email):
        return "Email invalido"
    # Padronizar username
    user["username"] = user["username"].strip().lower()
    # Formatar telefone
    user["telefone"] = re.sub(r"[^\d]", "", user["telefone"])
    # Extrair CEP
    endereco = user["endereco"]
    cep_match = re.search(r"\d{5}-\d{3}", endereco)
    if cep_match:
        user["cep"] = cep_match.group()
    else:
        user["cep"] = None
    
    return user

user = {
    "nome_completo": "JOÃO DA SILVA",
    "email": "joao.silva@exemplo.com",
    "username": "Joao_Silva123 ",
    "telefone": "(51) 99999-9999",
    "endereco": "Rua das Flores, 123, Bairro Centro, 90000-000, Porto Alegre - RS"
}

print(correct_user_register(user))