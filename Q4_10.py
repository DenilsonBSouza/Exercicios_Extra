class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, dist):
        combustivel_necessario = dist / self.consumo

        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print("O carro percorreu", dist, "km.")
        else:
            print("O carro não tem combustível suficiente para percorrer a distância desejada.")

    def abastecer(self, qtde):
        self.combustivel += qtde
        print("O carro foi abastecido com", qtde, "litros de combustível.")

carro1 = Carro(12)  
carro1.abastecer(20) 
carro1.andar(250)  
print("Quantidade de combustível no tanque:", carro1.combustivel, "litros")
