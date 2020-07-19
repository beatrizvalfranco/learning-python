def main():
    x = int(input())

    if x%2 == 0:
        x = x + 1 
    
    for _ in range(6): ## quando a variavel nao eh importante, eh uma boa pratica usar _ (underscore)
        print(x)
        x = x + 2

if __name__ == "__main__":
    main()