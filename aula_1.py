class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"


def mostrar_valores(*objts):
    for objeto in objts:
        print (objeto)

aiko = Estudante("Aiko", 545454)
fatima = Estudante("Fatima", 565656)
mostrar_valores(aiko, fatima)

aiko.numero = 555555
mostrar_valores(aiko, fatima)

