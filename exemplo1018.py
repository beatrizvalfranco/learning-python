def main():
    entrada = int(input())

    notas_100 = int(entrada/100)

    notas_50 = int(entrada%100/50)

    notas_20 = int(entrada%100%50/20)

    notas_10 = int(entrada%100%50%20/10)

    notas_5 = int(entrada%100%50%20%10/5)

    notas_2 = int(entrada%100%50%20%10%5/2)

    notas_1 = int(entrada%100%50%20%10%5%2)


    print(str(entrada) + "\n" +
        str(notas_100) + " nota(s) de R$ 100,00" + "\n" +
        str(notas_50) + " nota(s) de R$ 50,00" + "\n" +
        str(notas_20) + " nota(s) de R$ 20,00" + "\n" +
        str(notas_10) + " nota(s) de R$ 10,00" + "\n" +
        str(notas_5) + " nota(s) de R$ 5,00" + "\n" +
        str(notas_2) + " nota(s) de R$ 2,00" + "\n" +
        str(notas_1) + " nota(s) de R$ 1,00"
    )
        

if __name__ == "__main__":
    main()
