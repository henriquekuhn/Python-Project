'''
Você deve implementar um sistema de login que valide o nome de 
usuário e a senha com base nas seguintes regras:

Nome de Usuário:
    Deve ter entre 5 e 15 caracteres.
    Deve conter apenas letras e números.
    Deve começar com uma letra.

Senha:
    Deve ter entre 8 e 20 caracteres.
    Deve conter pelo menos uma letra maiúscula, uma letra minúscula, e um número.
    Não deve conter caracteres especiais.

Se o nome de usuário e a senha forem válidos, o sistema deve permitir o login; 
caso contrário, deve retornar a mensagem de erro adequada.
'''

from main import login

def equivalence_class():
    test = login()

    # valores usuários inválidos:
    assert test.validar_login("Rosb", "SenhaSegura1"), "Erro: O nome de usuário deve ter entre 5 e 15 caracteres."
    assert test.validar_login("RosbiffRosbiffRosbiff", "SenhaSegura1"), "Erro: O nome de usuário deve ter entre 5 e 15 caracteres."
    assert test.validar_login("Rosbiff@", "SenhaSegura1"), "Erro: O nome de usuário deve conter apenas letras e números."
    assert test.validar_login("8Rosbiff", "SenhaSegura1"), "Erro: O nome de usuário deve começar com uma letra."

    # valores senhas inválidas:
    assert test.validar_login("Rosbiff", "S3cur"), "Erro: A senha deve ter entre 8 e 20 caracteres."
    assert test.validar_login("Rosbiff", "SenhaMuitoSeguraComMaisDe20Caracteres1"), "Erro: A senha deve ter entre 8 e 20 caracteres."
    assert test.validar_login("Rosbiff", "senhasegura1"), "Erro: A senha deve conter pelo menos uma letra maiúscula."
    assert test.validar_login("Rosbiff", "SENHASEGURA1"), "Erro: A senha deve conter pelo menos uma letra minúscula."
    assert test.validar_login("Rosbiff", "SenhaSegura"), "Erro: A senha deve conter pelo menos um número."
    assert test.validar_login("Rosbiff", "SenhaSegura!") == "Erro: A senha não deve conter caracteres especiais."

    # Teste de usuário válido e senha válida
    assert test.validar_login("Henrique7", "SenhaSegura1") == "Login permitido"