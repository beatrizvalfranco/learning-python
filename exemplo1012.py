def main():
    entrada = input().split()
    
    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2]) 

    area_triangulo = (a * c)/2 
    
    pi = 3.14159
    
    area_circulo = pi * (c ** 2) 
    
    area_trapezio = ((a + b) * c)/2

    area_quadrado = b ** 2

    area_retangulo = a * b

    print(
        "TRIANGULO: " + str("%.3f"%area_triangulo) + "\n" +
        "CIRCULO: " + str("%.3f"%area_circulo) + "\n" +
        "TRAPEZIO: " + str("%.3f"%area_trapezio) + "\n" +
        "QUADRADO: " + str("%.3f"%area_quadrado) + "\n" +
        "RETANGULO: "+ str("%.3f"%area_retangulo)
        )


if __name__ == "__main__":
    main()