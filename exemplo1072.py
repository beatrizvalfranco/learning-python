def main():
    n = int(input())
 
    
    num_in_interval = 0


    for i in range(n):
        x = int(input())
        
        if x in range(10,20):
            num_in_interval += 1
        
        
    print(str(num_in_interval) + " in")
    print(str(n - num_in_interval) + " out")

        

if __name__ == "__main__":
    main()