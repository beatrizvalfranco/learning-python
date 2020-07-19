def main():
    N = int(input())

    for i in range(N):
        infos = input()
        splitted_infos = infos.split()
        name = splitted_infos[0]

        if name == "Thor":
            print("Y")
            continue     
        print ("N")


if __name__ == "__main__":
    main()