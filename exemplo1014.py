def main():
    x = int(input())
    y = float(input())

    consumo = x/y

    print(str("%.3f"%consumo) + " km/l")



if __name__ == "__main__":
    main()