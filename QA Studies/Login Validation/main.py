import re

class login:
    def validar_login(usuario: str, senha: str) -> str:
        # Validação do nome de usuário
        if not (5 <= len(usuario) <= 15):
            return "Erro: O nome de usuário deve ter entre 5 e 15 caracteres."
        if not usuario[0].isalpha():
            return "Erro: O nome de usuário deve começar com uma letra."
        if not usuario.isalnum():
            return "Erro: O nome de usuário deve conter apenas letras e números."

        # Validação da senha
        if not (8 <= len(senha) <= 20):
            return "Erro: A senha deve ter entre 8 e 20 caracteres."
        if not re.search("[A-Z]", senha):
            return "Erro: A senha deve conter pelo menos uma letra maiúscula."
        if not re.search("[a-z]", senha):
            return "Erro: A senha deve conter pelo menos uma letra minúscula."
        if not re.search("[0-9]", senha):
            return "Erro: A senha deve conter pelo menos um número."
        if re.search("[^a-zA-Z0-9]", senha):
            return "Erro: A senha não deve conter caracteres especiais."

        return "Login permitido"