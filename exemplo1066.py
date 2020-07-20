def main():
    
    even = 0
    odd = 0
    positive = 0 
    negative = 0
    for i in range(0,5):
        x = int(input())

        if x%2 == 0:
            even += 1
        elif x%2 == 1:
            odd += 1
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1

    print(str(even) + " valor(es) par(es)")
    print(str(odd) + " valor(es) impar(es)")
    print(str(positive) + " valor(es) positivo(s)")
    print(str(negative) + " valor(es) negativo(s)")

if __name__ == "__main__":
    main()