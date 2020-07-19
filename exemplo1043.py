def main():
    points = input().split()

    a = float(points[0])
    b = float(points[1])
    c = float(points[2])

    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Perimetro = " + str(a+b+c))
        return 
    print("Area = " + str(((a+b)*c)/2)) 

if __name__ == "__main__":
    main()