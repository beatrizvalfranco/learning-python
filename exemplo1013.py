def main():
    entrada = input().split()

    a = int(entrada[0])
    b = int(entrada[1])
    c = int(entrada[2])

    maior_ab = (a + b + abs(a - b))/2

    new_maior = (maior_ab + c + abs(maior_ab - c))/2

    print(str(int(new_maior)) + " eh o maior")

if __name__ == "__main__":
    main()