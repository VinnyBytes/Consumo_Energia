# Programa 
import time # para poder utilizar o comando time.sleep(uma pausa antes de mostrar algo)

# Dados de entrada
 
print("******CALCULE O CONSUMO MENSAL DO SEU APARELHO E SAIBA QUANTO ELE PESA NA SUA CONTA!******")
while True: # loop para que o programa continue rodando até que o usuário decida parar

    Nome_Aparelho = input("Digite o nome do aparelho que deseja saber o consumo: ")
    try:
     Potencia = float(input("Digite a potência do aparelho: "))
     Hora_Dia = float(input("Agora digite a quantidade de horas por dia em que o aparelho fica ligado: "))
    except ValueError: 
        print("Por favor, digite um valor numérico válido")
        continue  # Reinicia o loop para solicitar os valores novamente
# Processamento
    Consumo = (Potencia*Hora_Dia)/1000
    Valor_Estimado = (Consumo*0.93)

# Saída
    print("Aguarde um momento, estamos calculando o seu consumo mensal")
    time.sleep(2)
    print(f"O consumo mensal estimado para {Nome_Aparelho} é de: {Consumo:.2f}KWh.")
    time.sleep(2)
    print(f"O Valor estimado na conta para {Nome_Aparelho} é de: R${Valor_Estimado:.2f}.")

    continuar = input("Deseja calcular o consumo de outro aparelho? (Digite 'ENTER' caso queria continuar ou 'n' caso não queira): ")
    if continuar.lower() == "n":
        print("Obrigado por utilizar o programa!")
        break   #encerra o loop e finaliza o programa