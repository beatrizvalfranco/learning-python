def main():
    x = int(input())
    y = int(input())

    sum_odds = 0


    for i in range(min(x,y)+1, max(x,y)):
        if i%2 == 1:
            sum_odds += i
    
    print(sum_odds)
    


if __name__ == "__main__":
    main()