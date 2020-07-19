def main():
    entrada1 = input().split()
    entrada2 = input().split()
    
    code1 = int(entrada1[0])
    qtd1 = int(entrada1[1])
    price1 = float(entrada1[2])

    code2 = int(entrada2[0])
    qtd2 = int(entrada2[1])
    price2 = float(entrada2[2])
  

    total = (qtd1 * price1) + (qtd2 * price2)
    print("VALOR A PAGAR: R$ " + "%.2f"%total)

if __name__ == "__main__":
    main()