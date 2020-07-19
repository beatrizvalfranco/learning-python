def main():
    entrada = float(input())

    notas_100 = int(entrada/100)

    notas_50 = int(entrada%100/50)

    notas_20 = int(entrada%100%50/20)

    notas_10 = int(entrada%100%50%20/10)

    notas_5 = int(entrada%100%50%20%10/5)

    notas_2 = int(entrada%100%50%20%10%5/2)

    moedas_1 = int(entrada%100%50%20%10%5%2/1)

    moedas_050 = int(entrada%100%50%20%10%5%2%1/0.50)

    moedas_025 = int(entrada%100%50%20%10%5%2%1%0.50/0.25)

    moedas_010 = int(entrada%100%50%20%10%5%2%1%0.50%0.25/0.10)

    moedas_005 = int(entrada%100%50%20%10%5%2%1%0.50%0.25%0.10/0.05)

    moedas_001 = int(entrada%100%50%20%10%5%2%1%0.50%0.25%0.10%0.05/0.01)


    print("NOTAS: " + "\n" +
        str(notas_100) + " nota(s) de R$ 100.00" + "\n" +
        str(notas_50) + " nota(s) de R$ 50.00" + "\n" +
        str(notas_20) + " nota(s) de R$ 20.00" + "\n" +
        str(notas_10) + " nota(s) de R$ 10.00" + "\n" +
        str(notas_5) + " nota(s) de R$ 5.00" + "\n" +
        str(notas_2) + " nota(s) de R$ 2.00" + "\n" +
        "MOEDAS: " + "\n" +
        str(moedas_1) + " moeda(s) de R$ 1.00" + "\n" +
        str(moedas_050) + " moeda(s) de R$ 0.50" + "\n" +
        str(moedas_025) + " moeda(s) de R$ 0.25" + "\n" +
        str(moedas_010) + " moeda(s) de R$ 0.10" + "\n" +
        str(moedas_005) + " moeda(s) de R$ 0.05" + "\n" +
        str(moedas_001) + " moeda(s) de R$ 0.01" + "\n"
    )
        

if __name__ == "__main__":
    main()