def main():
    two_values = input().split()

    A = int(two_values[0])
    B = int(two_values[1])

    if A%B == 0 or B%A == 0:
        print("Sao Multiplos")
        return
    print("Nao sao Multiplos" )

if __name__ == "__main__":
    main()