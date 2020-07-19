def main():
    tempo = int(input())
    velocidade = int(input())
    distancia = tempo * velocidade
    litros = distancia/12
    print ('%.3f'%(litros))

if __name__ == "__main__":
    main()