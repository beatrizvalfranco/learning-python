def main():
    x = input().split()
    
    for i in range(len(x)):
        x[i] = int(x[i])

    asc_order = sorted(x)
    
    for i in asc_order:
        print(i)
    
    print("")

    for i in x:
        print(i)
  
    

if __name__ == "__main__":
    main()