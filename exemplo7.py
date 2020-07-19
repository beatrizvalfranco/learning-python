def main():
    entrada = input().split()
    code = int(entrada[0])
    qtd = int(entrada[1])
    
    prices = [
        [1,4],
        [2, 4.5],
        [3, 5],
        [4, 2],
        [5, 1.5],
    ]
    price = 0
    for p in prices:
        if p[0] == code:
            price = p[1]
            break

    total = price * qtd
    print ("Total: R$ %.2f" % total)

if __name__ == "__main__":
    main()