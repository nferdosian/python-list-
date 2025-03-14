# Data Entry: Initialize the weekly_expenses list
weekly_expenses = [15.00, 12.50, 20.00, 18.75, 22.00, 25.50, 19.25]

# Function to calculate total expenditure
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

# Function to find the highest expense
def find_highest_expense(expenses):
    highest = expenses[0]
    for expense in expenses:
        if expense > highest:
            highest = expense
    return highest

# Function to count occurrences of a specific expense
def count_expense_occurrences(expenses, amount):
    count = 0
    for expense in expenses:
        if expense == amount:
            count += 1
    return count

# Function to remove duplicate expenses
def remove_duplicates(expenses):
    unique_expenses = []
    for expense in expenses:
        if expense not in unique_expenses:
            unique_expenses.append(expense)
    return unique_expenses

# Function to reverse the expense list
def reverse_expenses(expenses):
    reversed_list = []
    for i in range(len(expenses) - 1, -1, -1):
        reversed_list.append(expenses[i])
    return reversed_list

# Call functions and display results
# 1. Total expenditure
total_expenditure = calculate_total(weekly_expenses)
print(f"Total expenditure for the week: €{total_expenditure:.2f}")

# 2. Highest single-day expense
highest_expense = find_highest_expense(weekly_expenses)
print(f"Highest single-day expense: €{highest_expense:.2f}")

# 3. Number of times a specific expense (e.g., €20.00) occurs
specific_expense = 20.00
occurrences = count_expense_occurrences(weekly_expenses, specific_expense)
print(f"The amount €{specific_expense:.2f} was spent {occurrences} time(s).")

# 4. List of unique expenses
unique_expenses = remove_duplicates(weekly_expenses)

formatted_expenses = []
for expense in unique_expenses:
    formatted_expenses.append(f"€{expense:.2f}")

print("List of unique expenses:", formatted_expenses)
# 5. Expenses in reverse order
reversed_expenses = reverse_expenses(weekly_expenses)
# Initialize an empty list to store formatted reversed expenses
formatted_reversed_expenses = []
for expense in reversed_expenses:
    formatted_reversed_expenses.append(f"€{expense:.2f}")
    
print("Expenses in reverse order:", formatted_reversed_expenses)





#-------------------------------------second version-----------------------------------------------------------


# writing the above program with 'list comprehension' method
# Data Entry: Initialize the weekly_expenses list

# Function to find the highest expense
def find_highest_expense(expenses):
    highest = expenses[0]
    for expense in expenses:
        if expense > highest:
            highest = expense
    return highest

# Function to count occurrences of a specific expense
def count_expense_occurrences(expenses, amount):
    count = 0
    for expense in expenses:
        if expense == amount:
            count += 1
    return count

# Function to remove duplicate expenses
def remove_duplicates(expenses):
    unique_expenses = []
    for expense in expenses:
        if expense not in unique_expenses:
            unique_expenses.append(expense)
    return unique_expenses

# Function to reverse the expense list
def reverse_expenses(expenses):
    reversed_list = []
    for i in range(len(expenses) - 1, -1, -1):
        reversed_list.append(expenses[i])
    return reversed_list

# Call functions and display results
# 1. Total expenditure
total_expenditure = calculate_total(weekly_expenses)
print(f"Total expenditure for the week: €{total_expenditure:.2f}")

# 2. Highest single-day expense
highest_expense = find_highest_expense(weekly_expenses)
print(f"Highest single-day expense: €{highest_expense:.2f}")

# 3. Number of times a specific expense (e.g., €20.00) occurs
specific_expense = 20.00
occurrences = count_expense_occurrences(weekly_expenses, specific_expense)
print(f"The amount €{specific_expense:.2f} was spent {occurrences} time(s).")

# 4. List of unique expenses
unique_expenses = remove_duplicates(weekly_expenses)
print(f"List of unique expenses: {[f'€{expense:.2f}' for expense in unique_expenses]}")

# 5. Expenses in reverse order
reversed_expenses = reverse_expenses(weekly_expenses)
print(f"Expenses in reverse order: {[f'€{expense:.2f}' for expense in reversed_expenses]}")



#------------------------------------------third version-----------------------------------------------

#change made here is asking user to input their list of expenses and specific expense,
#rather than a constant give expense list to to program

# Read weekly expenses from user input
print("Enter your daily expenses for the week (Monday to Sunday):")
weekly_expenses = []
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    expense = float(input(f"Enter expense for {day}: "))
    weekly_expenses.append(expense)

# Function to calculate total expenditure
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

# Function to find the highest expense
def find_highest_expense(expenses):
    highest = expenses[0]
    for expense in expenses:
        if expense > highest:
            highest = expense
    return highest

# Function to count occurrences of a specific expense
def count_expense_occurrences(expenses, amount):
    count = 0
    for expense in expenses:
        if expense == amount:
            count += 1
    return count

# Function to remove duplicate expenses
def remove_duplicates(expenses):
    unique_expenses = []
    for expense in expenses:
        if expense not in unique_expenses:
            unique_expenses.append(expense)
    return unique_expenses

# Function to reverse the expense list
def reverse_expenses(expenses):
    reversed_list = []
    for i in range(len(expenses) - 1, -1, -1):
        reversed_list.append(expenses[i])
    return reversed_list

# Call functions and display results
# 1. Total expenditure
total_expenditure = calculate_total(weekly_expenses)
print(f"Total expenditure for the week: €{total_expenditure:.2f}")

# 2. Highest single-day expense
highest_expense = find_highest_expense(weekly_expenses)
print(f"Highest single-day expense: €{highest_expense:.2f}")

# 3. Number of times a specific expense occurs
specific_expense = float(input("Enter a specific expense amount to count: "))
occurrences = count_expense_occurrences(weekly_expenses, specific_expense)
print(f"The amount €{specific_expense:.2f} was spent {occurrences} time(s).")

# 4. List of unique expenses
unique_expenses = remove_duplicates(weekly_expenses)
print(f"List of unique expenses: {[f'€{expense:.2f}' for expense in unique_expenses]}")

# 5. Expenses in reverse order
reversed_expenses = reverse_expenses(weekly_expenses)
print(f"Expenses in reverse order: {[f'€{expense:.2f}' for expense in reversed_expenses]}")


 





