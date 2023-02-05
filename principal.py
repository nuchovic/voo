from voo import Flight

print("Bem Vindo ao Voa Comigo")
vc = int(input("Defina a Capacidade do Voo "))

emirates = Flight(vc)

for i in range(10):
    name = input("Nome do Passageiro: ")
    if emirates.add_passengers(name):
        print(f"{name} Passageiro Adicionado com Sucesso")
    else:
        print(f"Nao eh Possivel Adicional {name} no Voo, Voo Cheio")   