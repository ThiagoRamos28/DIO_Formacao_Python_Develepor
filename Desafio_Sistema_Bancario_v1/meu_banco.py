menu = """
========== SERVIÇOS DISPONÍVEIS ==========
|                                        |
| [1] - Depositar                        |
| [2] - Sacar                            |
| [3] - Extrato                          |
| [4] - Finalizar Sessão                 |
|                                        |
==========================================

=> Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o seu limite diário disponível.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários foi atingindo.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 4:
        print("Obrigado por ser nosso cliente, Volte Sempre.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
