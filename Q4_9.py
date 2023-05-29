class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


funcionario1 = Funcionario("João", 2500.0)

print("Nome:", funcionario1.nome)
print("Salário:", funcionario1.salario)
