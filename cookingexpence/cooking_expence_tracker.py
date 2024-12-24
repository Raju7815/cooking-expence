import json

# Function to load expenses from a file
def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save expenses to a file
def save_expenses(filename, expenses):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense(expenses, item, cost):
    expenses.append({'item': item, 'cost': cost})

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"Item: {expense['item']}, Cost: {expense['cost']}")

# Function to calculate the total expenses
def calculate_total(expenses):
    return sum(expense['cost'] for expense in expenses)

def main():
    filename = 'expenses.json'
    expenses = load_expenses(filename)

    while True:
        print("\nCooking Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item: ")
            cost = float(input("Enter the cost: "))
            add_expense(expenses, item, cost)
            save_expenses(filename, expenses)
            print("Expense added successfully.")
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total = calculate_total(expenses)
            print(f"Total Expenses: {total}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
