
saldo = 10000000
LIMITE_SAQUES = 3
numero_saques = 0
limite = 500
extrato = ""

def menu():
    print("==Sistema Bancário==".center(20, " "))
    print(f"saldo: R$ {saldo:.2f}".center(20, " "))
    print("==MENU==".center(20, " "))
    print("1. Sacar ".center(20, " "))
    print("2. Depositar ".center(20, " "))
    print("3. Ver saldo ".center(20, " "))
    print("4. Extrato ".center(20, " "))
    print("5. Sair ".center(20, " "))


def saque():
    global saldo
    global numero_saques
    global extrato
    while True:
        valor_saque = input("Informe o valor do saque: ")
        try:
            valor_saque = float(valor_saque)
            if valor_saque > saldo:
                print("saldo insuficiente")
                break
            elif valor_saque > limite:
                print("valor acima do limite")
                break
            elif valor_saque < 0:
                print("valor invalido, apenas valores positivos")
                break
            if numero_saques >= LIMITE_SAQUES:
                print("limite de saques atingido")
                break
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print(f"Seu saldo agora é: R$ {saldo:.2f}")
                print("saque efetuado com sucesso")
                break
        except ValueError:
            print("valor invalido, apenas numeros")

    else:
       pass

def depositar():
    global saldo
    global extrato
    while True:
        valor_deposito = input("Informe o valor do Deposito:")
        try:
           valor_deposito = float(valor_deposito)
           if valor_deposito <= 0:
               print("valor invalido, apenas numeros") 
           else:
               saldo += valor_deposito
               extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
               print("Depósito realizado!")
               print(f"Seu saldo agora é: R$ {saldo:.2f}")
               return saldo
        except ValueError:
               print("valor invalido, apenas numeros")
    else:
        pass

def main():
    global saldo
    while True:
      menu()
      opcao = input("Selecione uma ação: ")  
      if opcao == "1":
           saque()
      elif opcao == "2":
          depositar()
      elif opcao == "3":
            print(f"Seu saldo é: R$ {saldo:.2f}")
      elif opcao == "4":
            print("Extrato:")
            if extrato == "":
                print("Não foram realizadas movimentações.")
            else:
              print(extrato)
              print(f"Seu saldo é: R$ {saldo:.2f}")
      elif opcao == "5":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()