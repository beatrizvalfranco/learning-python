def main():
    salario = float(input())

    if salario <= 2000:
        print("Isento")
    elif salario > 2000 and salario <= 3000:
        print("R$ " + str("%.2f"%((salario - 2000) * 8/100)))
    elif salario > 3000 and salario <= 4500:
        print("R$ " + str("%.2f"%(((salario - 3000) * 18/100) + 80)))
    elif salario > 4500:
        print("R$ " + str("%.2f"%(((salario - 4500) * 28/100) + 80 + 270)))

if __name__ == "__main__":
    main()