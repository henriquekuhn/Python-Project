'''
- A idade deve ser um número inteiro entre 18 e 99.
- Idades fora desse intervalo devem ser consideradas inválidas.
- O sistema deve retornar uma mensagem apropriada se a idade for válida ou inválida.
'''
class test_studies:
    def valida_idade(self, idade: int) -> str:
        if not isinstance(idade, int):
            return "Idade inválida: deve ser um número inteiro."
        if 18 <= idade <= 99:
            return "Idade válida."
        else:
            return "Idade inválida: fora do intervalo permitido."