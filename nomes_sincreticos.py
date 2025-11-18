# Exemplo de sincretismo de nomes próprios

class NomeSincretico:
    def __init__(self, nome1, nome2):
        self.nome1 = nome1
        self.nome2 = nome2

    def __str__(self):
        return f'{self.nome1}-{self.nome2}'

nome = NomeSincretico('Maria', 'Luzia')
print(nome)