menu = """
======================================
    SEJA BEM VINDO AO BANCO D.I.O
======================================

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

======================================

-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na Operação! Valor informado é invalido!")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na Operação! Saldo insuficiente!")

        elif excedeu_limite:
            print("Falha na Operação! O valor informado ultrapassa do seu limite!")

        elif excedeu_saques:
            print("Falha na Operação! Limite de saques excedido, tente novamente mais tarde!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na Operação! Valor informado é invalido!")

    elif opcao == "3":
        print("\n=========================================")
        print("\n====            EXTRATO              ====")
        print("\n=========================================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "0":
        break

    else:
        print("Falha na Operação, por favor selecione uma das opções acima.")