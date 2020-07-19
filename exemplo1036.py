import math 

def main():
    entrada = input().split()

    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2])

    delta = (pow(b, 2)) - (4*a*c)

    if a == 0:
        print("Impossivel calcular")

    elif delta < 0:
        print("Impossivel calcular")
    
    else: 
        r1 = (-b + math.sqrt(delta))/(2 * a)
        r2 = (-b - math.sqrt(delta))/(2 * a)
        print("R1 = " + str("%.5f"%r1) + "\n" + "R2 = " + str("%.5f"%r2))

if __name__ == "__main__":
    main()