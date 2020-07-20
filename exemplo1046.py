def main():
    start_end_game = input().split()

    start = int(start_end_game[0])
    end = int(start_end_game[1])

    if end<start or start == end:
        end = end + 24
  
    print("O JOGO DUROU " + str(end - start) + " HORA(S)")


if __name__ == "__main__":
    main()