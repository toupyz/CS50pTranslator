import csv
import matplotlib.pyplot as plt
from collections import defaultdict


filename = "expenses.csv"
# Input validation
def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if value.isalpha():
            return value
        else:
            print("Invalid input. Please enter letters only (e.g. 'food').")

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main functions
def add_expense(filename="expenses.csv"):
    expense_type = get_valid_string("Enter expense type (e.g. fun, food, bills): ")
    expense_cost = get_valid_float("Enter how much it was: ")

    expense_data = {
        "type": expense_type,
        "amount": expense_cost
    }

    # Check if file exists to decide whether to write headers
    try:
        with open(filename, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    # Write the data
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=expense_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense_data)

    print("Expense added successfully!")


def remove_expense():
    try:
        with open(filename, mode='r', newline='') as file:
            reader = list(csv.DictReader(file))
    except FileNotFoundError:
        print("No expenses found. File does not exist.")
        return

    if not reader:
        print("No expenses to remove.")
        return

    # Ask for details to match
    expense_type = input("Enter the expense type to remove (e.g. food, fun): ").strip().lower()
    try:
        expense_amount = float(input("Enter the expense amount to remove: "))
    except ValueError:
        print("Invalid amount. Must be a number.")
        return

    # Search for matching expense(s)
    matched = [
        (i, row) for i, row in enumerate(reader)
        if row['type'].strip().lower() == expense_type and float(row['amount']) == expense_amount
    ]

    if not matched:
        print("No matching expense found.")
        return

    # Remove first matched (or all if you prefer)
    index_to_remove, removed = matched[0]
    del reader[index_to_remove]

    # Write updated list back
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=removed.keys())
        writer.writeheader()
        writer.writerows(reader)

    print(f"Removed expense: Type: {removed['type']} | Amount: {removed['amount']}")



def view_expense():
    print("")
    with open(filename, mode='r', newline='') as file:
        for line in file:
            print(line)




def plot_expenses(filename="expenses.csv"):
    expenses_by_type = defaultdict(float)

    # Read the expenses CSV and sum amounts by type
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses_by_type[row['type']] += float(row['amount'])
    except FileNotFoundError:
        print("No expenses file found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not expenses_by_type:
        print("No expenses to plot.")
        return

    # Prepare data for plotting
    categories = list(expenses_by_type.keys())
    amounts = list(expenses_by_type.values())

    # Plot
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nWelcome to the Finance Tracker!")
        print("1. Add expense")
        print("2. Remove expense")
        print("3. View expenses")
        print("4. View expense graph")
        print("5. Exit")

        try:
            user_input = int(input("What do you want to do? (Enter number): "))
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            continue

        if user_input == 1:
            add_expense()
        elif user_input == 2:
            remove_expense()
        elif user_input == 3:
            view_expense()  # Make sure you define this!
        elif user_input == 4:
            plot_expenses()
        elif user_input == 5:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option (1-4).")


if __name__ == "__main__":
    main()