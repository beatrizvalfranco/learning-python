def main():

    even = 0

    for i in range(0,5):
        x = int(input())
        
        if x%2 == 0:
            even += 1
        
        
    print(str(even) + " valores pares")
 

if __name__ == "__main__":
    main()