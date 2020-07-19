def main():
    number = int(input())
    hours_worked = int(input())
    salary_per_hour = float(input())

    total_salary = hours_worked * salary_per_hour
    
    print(
        "NUMBER = " + str(number) + "\n" +
        "SALARY = U$ " + str("%.2f"%total_salary)
    )


if __name__ == "__main__":
    main()