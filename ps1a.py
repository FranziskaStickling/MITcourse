# Ask for user inputs and cast to floats
annual_salary = float(input("Enter annual salary:"))
portion_saved = float(input("Enter portion of salary to be saved i.e. 0.1 for 10%:"))
total_cost = float(input("Enter total cost of dream house:"))

# Given:
portion_down_pament = 0.25
r = 0.04

# further calculaitons
salary_savings_month = (annual_salary * portion_saved)/12

current_savings = 0
number_of_month = 0
# invest_return = current_savings*r/12

while current_savings < total_cost:
    current_savings = current_savings + salary_savings_month
    number_of_month = number_of_month + 1
    if current_savings >= total_cost:
        break
print('Number of month: ', number_of_month)
