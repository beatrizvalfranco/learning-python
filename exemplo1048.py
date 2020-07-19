def main():
    salary = float(input())

    if salary >= 0 and salary <= 400:
        print("Novo salario: " + str("%.2f"%(salary + (salary * 15/100))))
        print("Reajuste ganho: " + str("%.2f"%(salary * 15/100)))
        print("Em percentual: 15 %")
    
    elif salary > 400 and salary <= 800:
        print("Novo salario: " + str("%.2f"%(salary + (salary * 12/100))))
        print("Reajuste ganho: " + str("%.2f"%(salary * 12/100)))
        print("Em percentual: 12 %")
    
    elif salary > 800 and salary <= 1200:
        print("Novo salario: " + str("%.2f"%(salary + (salary * 10/100))))
        print("Reajuste ganho: " + str("%.2f"%(salary * 10/100)))
        print("Em percentual: 10 %")
      
    elif salary > 1200 and salary <= 2000:
        print("Novo salario: " + str("%.2f"%(salary + (salary * 7/100))))
        print("Reajuste ganho: " + str("%.2f"%(salary * 7/100)))
        print("Em percentual: 7 %")
        
    elif salary > 2000:
        print("Novo salario: " + str("%.2f"%(salary + (salary * 4/100))))
        print("Reajuste ganho: " + str("%.2f"%(salary * 4/100)))
        print("Em percentual: 4 %")

if __name__ == "__main__":
    main()