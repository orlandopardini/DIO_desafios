saldo = 1500.00
limite_saque = 500.00
saques_diarios = 0
limite_saques = 3
extrato = []

while True:
    print("\n--- Menu ---")
    print("1 - Realizar saque")
    print("2 - Ver extrato")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if saques_diarios >= limite_saques:
            print("Você já realizou o número máximo de saques hoje.")
        
            continue
        valor = float(input("Digite o valor do saque: R$ "))
        if valor > saldo:
            print("Não será possível sacar o dinheiro por falta de saldo.")
        elif valor > limite_saque:
            print("Valor do saque excede o limite de R$ 500,00 por saque.")
        else:
            saldo -= valor
            saques_diarios += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "2":
        print("\n--- Extrato ---")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for item in extrato:
                print(item)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "3":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
