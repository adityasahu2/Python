# 1. Write a Python function basic_salary that accepts two parameters: hourly_rate and hours_worked_per_week. The function should calculate the basic salary per month (assuming a month has 4 weeks). If the hours worked per week exceed 40, create another function overtime_salary, where every extra hour worked is paid at 1.5 times the normal hourly rate. Finally, create another function total_salary that returns the sum of the basic salary and overtime.
def basic_salary(hourly_rate, hours_per_week):
    return min(hours_per_week, 40) * hourly_rate * 4

def overtime_salary(hourly_rate, hours_per_week):
    overtime_hours = max(0, hours_per_week - 40)
    return overtime_hours * hourly_rate * 1.5 * 4

def total_salary(hourly_rate, hours_per_week):
    return basic_salary(hourly_rate, hours_per_week) + overtime_salary(hourly_rate, hours_per_week)

# 2.Create a function tax_amount that shows how much taxes are deducted from the basic salary. Taxes are applied as follows:
# • If the salary is less than Rs. 60,000/-, deduct 10% as tax.
# • If the salary is between Rs. 60,000/- and Rs. 85,000/-, deduct 15% as tax.
# • If the salary is more than Rs. 85,000/-, deduct 20% as tax.
def tax_amount(basic_salary):
    tax_brackets = [(60000, 0.10), (85000, 0.15), (float('inf'), 0.20)]
    for threshold, rate in tax_brackets:
        if basic_salary <= threshold:
            return basic_salary * rate

# 3. Using the function basic_salary from Question 1, write another function gross_salary that calculates the gross salary of an employee. This function should accept basic_salary as input (output from Question 1), consider a fixed value of allowances (e.g., 20% of basic salary), and return the gross salary (basic salary + allowances - tax).
def gross_salary(hourly_rate, hours_per_week):
    base = basic_salary(hourly_rate, hours_per_week)
    allowances = base * 0.20
    tax = tax_amount(base)
    return base + allowances - tax

# 4. Using the gross_salary function from Question 3, write a function salary_bracket that categorizes the employee’s gross salary into one of the following brackets:
# • ”Low income” if gross salary is below Rs. 50,000/-.
# • ”Middle income” if gross salary is between Rs. 50,000/- and Rs. 80,000/-.
# • ”High income” if gross salary is more than Rs. 80,000/-.
def salary_bracket(gross_salary):
    return ("Low income" if gross_salary < 50000 
            else "Middle income" if gross_salary <= 80000 
            else "High income")

# 5. Take three different sets of employee names, hourly rates and hours worked per week as user input. Write a Python function employee_report that generates a formatted report of all employees’ salary details. This function should print the employee names, basic salaries, gross salaries, tax amounts, and salary brackets in a readable format.
def employee_report():
    employees = []
    for i in range(3):
        name = input(f"Enter employee name {i+1}: ")
        hourly_rate = float(input(f"Enter hourly rate for {name}: "))
        hours_worked = int(input(f"Enter hours worked per week for {name}: "))
        employees.append([name, hourly_rate, hours_worked])
        print()

    for emp in employees:
        basic = basic_salary(emp[1], emp[2])
        gross = gross_salary(emp[1], emp[2])
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        
        print(f"\nEmployee Name: {emp[0]}")
        print(f"Basic Salary: Rs. {basic:.2f}")
        print(f"Gross Salary: Rs. {gross:.2f}")
        print(f"Tax Amount: Rs. {tax:.2f}")
        print(f"Salary Bracket: {bracket}")

employee_report()
