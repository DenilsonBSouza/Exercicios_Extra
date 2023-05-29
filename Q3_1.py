def valida_nome():
    while True:
        nome = input("Digite o seu nome: ")
        if len(nome) > 3:
            return nome
        else:
            print("O nome deverá ser maior que 3 caracteres, por favor, digite o nome com tamanho válido! \n")

def valida_idade():
    while True:
        idade = input("Digite a idade (entre 0 e 150): ")
        if idade.isdigit() and 0 <= int(idade) <= 150:
            return int(idade)
        else:
            print("A idade deve ser um número entre 0 e 150.\n")

def obter_salario():
    while True:
        salario = input("Digite o salário (maior que zero): ")
        if salario.replace('.', '', 1).isdigit() and float(salario) > 0:
            return float(salario)
        else:
            print("O salário deve ser um número maior que zero.\n")

def obter_sexo():
    while True:
        sexo = input("Digite o sexo (F/M): ")
        if sexo.upper() == 'F' or sexo.upper() == 'M':
            return sexo.upper()
        else:
            print("O sexo deve ser 'F' ou 'M'.\n")

def obter_estado_civil():
    while True:
        estado_civil = input("Digite o estado civil (S/C/V/D): ")
        if estado_civil.upper() in ['S', 'C', 'V', 'D']:
            return estado_civil.upper()
        else:
            print("O estado civil deve ser 'S', 'C', 'V' ou 'D'.\n")

def obter_informacoes():
    nome = valida_nome()
    idade = valida_idade()
    salario = obter_salario()
    sexo = obter_sexo()
    estado_civil = obter_estado_civil()

    print("\nInformações válidas:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Salário:", salario)
    print("Sexo:", sexo)
    print("Estado Civil:", estado_civil)

obter_informacoes() 