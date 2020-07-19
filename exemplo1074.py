def main():
    n = int(input())
    x = []

    for i in range(n):
        x.append(int(input()))
    
    for i in x: 
        if i == 0:
            print("NULL")
        elif i % 2 == 0:
            if i > 0:
                print("EVEN POSITIVE")
                continue
            print("EVEN NEGATIVE")
        else:
            if i > 0:
                print("ODD POSITIVE")
                continue
            print("ODD NEGATIVE")

if __name__ == "__main__":
    main()