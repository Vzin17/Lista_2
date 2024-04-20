import math

def calcular_preco(chegada, partida):
    minutos_chegada = chegada[0] * 60 + chegada[1]
    minutos_partida = partida[0] * 60 + partida[1]

    tempo_total = minutos_partida - minutos_chegada

    horas_a_pagar = math.ceil(tempo_total / 60)

    if horas_a_pagar <= 2:
        preco = horas_a_pagar * 1.00
    elif horas_a_pagar <= 4:
        preco = 2 * 1.00 + (horas_a_pagar - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (horas_a_pagar - 4) * 2.00

    return preco

def ler_momento(mensagem):
    hora, minuto = input(mensagem).split()
    return int(hora), int(minuto)

def main():
    chegada = ler_momento("Informe a hora de chegada (hh mm): ")
    partida = ler_momento("Informe a hora de partida (hh mm): ")

    preco = calcular_preco(chegada, partida)

    print("O preço cobrado pelo estacionamento é R$", preco)

if __name__ == "__main__":
    main()
