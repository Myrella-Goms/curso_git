print("---- Sistema de Cadastro ----")
print("------ Seja bem vindo ------")
nome = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

if age >= 18:
    print(f"Olá {nome}, cadastro feito com sucesso!")
elif age < 18:
    print ("Acesso negado")

while True:
    print("Gostaria de conhecer nossos serviços? ")
    resposta = input("Digite sim ou não: ")
    if resposta == "sim":
        print ("bem vinda à claro!")
    else:
        print ("entendido")
        break

