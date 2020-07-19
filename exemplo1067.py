def main():
    number = int(input())
    if number >= 1 and number <= 1000:
        for i in range(1, number + 1, 2):
            print(str(i))


if __name__ == "__main__":
    main()