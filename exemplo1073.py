def main():
    n = int(input())
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(str(i) + "^2 = " + str(i**2))

if __name__ == "__main__":
    main()