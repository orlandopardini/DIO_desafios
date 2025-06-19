from cliente import PessoaFisica
from conta import ContaCorrente
from transacoes import Deposito, Saque

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def main():
    cliente = PessoaFisica(
        cpf="12345678900",
        nome="Fulano",
        data_nascimento="2000-01-01",
        endereco="Rua Exemplo, 123"
    )
    conta = ContaCorrente(cliente, numero=1)
    cliente.adicionar_conta(conta)

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            deposito = Deposito(valor)
            cliente.realizar_transacao(conta, deposito)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saque = Saque(valor)
            cliente.realizar_transacao(conta, saque)

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            for transacao in conta.historico.transacoes:
                tipo = transacao.__class__.__name__
                print(f"{tipo}: R$ {transacao.valor:.2f}")
            print(f"\nSaldo: R$ {conta.saldo_atual():.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione novamente.")

if __name__ == "__main__":
    main()
