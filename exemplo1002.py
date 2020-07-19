def main():
    raio = float(input())

    pi = 3.14159

    area = pi * pow(raio, 2)

    print("A=" + str("%.4f"%area))

if __name__ == "__main__":
    main()