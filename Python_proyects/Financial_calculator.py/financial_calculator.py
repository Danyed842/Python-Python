def financial_calculator():
    #is a function who helps to reach goals
    monthly_income = float(input("put your monthly income(USD): "))
    monthly_expenses = float(input("put your monthly expenses(USD): "))
    goal = float(input("put a goal to reach (USD): "))
    savings = monthly_income - monthly_expenses
    months = goal // savings
    if savings <= 0:
        print(f"Hey, you're not saving money, be careful.")
    else:
        print(f"the months needed to reach your goal are: {months} months")



