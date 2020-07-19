def main():
    seller = str(input())
    fixed_salary = input()
    sales_amount = input()
    
    fixed_salary = float(fixed_salary)
    sales_amount = float(sales_amount)
    total = fixed_salary + (0.15*sales_amount)
    print("TOTAL = R$ " + str("%.2f"%total))

if __name__ == "__main__":
    main()