class Pessoa:
    def __init__(self, nome= None, idade= None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_de_idade(idade):
        return idade >= 18
    
p = Pessoa.criar_de_data_nascimento(2001, 5, 1, "Aiko")

print (p.nome, p.idade)

print (Pessoa.maior_de_idade(18))
print (Pessoa.maior_de_idade(14))
