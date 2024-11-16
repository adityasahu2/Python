# 1. Write a Python function basic_salary that accepts two parameters: hourly_rate and hours_worked_per_week. The function should calculate the basic salary per month (assuming a month has 4 weeks). If the hours worked per week exceed 40, create another function overtime_salary, where every extra hour worked is paid at 1.5 times the normal hourly rate. Finally, create another function total_salary that returns the sum of the basic salary and overtime.
def basic_salary(hourly_rate, hours_per_week):
    basic_hours = min(hours_per_week, 40)
    monthly_salary = basic_hours * hourly_rate * 4
    return monthly_salary

def overtime_salary(hourly_rate, hours_per_week):
    overtime_hours = max(hours_per_week - 40, 0)
    monthly_overtime = overtime_hours * (hourly_rate * 1.5) * 4
    return monthly_overtime

def total_salary(hourly_rate, hours_per_week):
    base = basic_salary(hourly_rate, hours_per_week)
    overtime = overtime_salary(hourly_rate, hours_per_week)
    return base + overtime

# 2.Create a function tax_amount that shows how much taxes are deducted from the basic salary. Taxes are applied as follows:
# • If the salary is less than Rs. 60,000/-, deduct 10% as tax.
# • If the salary is between Rs. 60,000/- and Rs. 85,000/-, deduct 15% as tax.
# • If the salary is more than Rs. 85,000/-, deduct 20% as tax.
def tax_amount(basic_salary):
    if basic_salary < 60000:
        tax = basic_salary * 0.10
    elif 60000 <= basic_salary <= 85000:
        tax = basic_salary * 0.15
    else:
        tax = basic_salary * 0.20
    return tax

# 3. Using the function basic_salary from Question 1, write another function gross_salary that calculates the gross salary of an employee. This function should accept basic_salary as input (output from Question 1), consider a fixed value of allowances (e.g., 20% of basic salary), and return the gross salary (basic salary + allowances - tax).
def gross_salary(hourly_rate, hours_per_week):
    base_salary = basic_salary(hourly_rate, hours_per_week)
    allowances = base_salary * 0.20
    tax = tax_amount(base_salary)
    gross = base_salary + allowances - tax
    return gross

# 4. Using the gross_salary function from Question 3, write a function salary_bracket that categorizes the employee’s gross salary into one of the following brackets:
# • ”Low income” if gross salary is below Rs. 50,000/-.
# • ”Middle income” if gross salary is between Rs. 50,000/- and Rs. 80,000/-.
# • ”High income” if gross salary is more than Rs. 80,000/-.
def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"
    
# 5. Take three different sets of employee names, hourly rates and hours worked per week as user input. Write a Python function employee_report that generates a formatted report of all employees’ salary details. This function should print the employee names, basic salaries, gross salaries, tax amounts, and salary brackets in a readable format.
def employee_report():
    names, hourly_rates, hours_worked_per_week = [],[],[]
    for i in range(3):
        names.append(input(f"Enter employee name {i+1}: "))
        hourly_rates.append(float(input(f"Enter hourly rate for {names[i]}: ")))
        hours_worked_per_week.append(int(input(f"Enter hours worked per week for {names[i]}: ")))

    for i in range(3):
        basic = basic_salary(hourly_rates[i], hours_worked_per_week[i])
        gross = gross_salary(hourly_rates[i], hours_worked_per_week[i])
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        print(f"\nEmployee Name: {names[i]}")
        print(f"Basic Salary: Rs. {basic:.2f}")
        print(f"Gross Salary: Rs. {gross:.2f}")
        print(f"Tax Amount: Rs. {tax:.2f}")
        print(f"Salary Bracket: {bracket}")

employee_report()
