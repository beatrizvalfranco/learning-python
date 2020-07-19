def main():
    idade = int(input())
    anos = idade/365
    meses = idade%365/30
    dias = idade%365%30

    print(str(int(anos)) + " ano(s)" + "\n" + str(int(meses)) + " mes(es)" + "\n" + str(int(dias)) + " dia(s)")

if __name__ == "__main__":
    main()