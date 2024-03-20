import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount, date):
        if category in self.expenses:
            self.expenses[category].append((amount, date))
        else:
            self.expenses[category] = [(amount, date)]

    def get_total_spending(self):
        total = 0
        for category in self.expenses:
            for amount, _ in self.expenses[category]:
                total += amount
        return total

    def get_category_spending(self, category):
        if category in self.expenses:
            return sum(amount for amount, _ in self.expenses[category])
        else:
            return 0

    def view_spending_patterns(self):
        print("Spending Patterns:")
        for category in self.expenses:
            total_spending = sum(amount for amount, _ in self.expenses[category])
            print("--------Your Spending Amount---------")
            print(f"{category}: {total_spending}/-")
            print("-------------------------------------")
        print()

    def view_expenses_by_date(self, date):
        print(f"Expenses on {date}:")
        expenses_found = False
        for category in self.expenses:
            expenses_on_date = [amount for amount, expense_date in self.expenses[category] if expense_date == date]
            if expenses_on_date:
                total_spending = sum(expenses_on_date)
                print(f"{category}: {total_spending}/-")
                expenses_found = True
        if not expenses_found:
            print("None")
        print()

def main():
    tracker = ExpenseTracker()

    while True:
        print("1. Add Expense")
        print("2. View Spending Patterns")
        print("3. View Total Spending")
        print("4. View Expenses by Date")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("----------Enter expense category----------")
            amount = float(input("Enter expense amount: "))
            date_input = input("Enter expense date (YYYY-MM-DD): ")
            expense_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            tracker.add_expense(category, amount, expense_date)
        elif choice == "2":
            tracker.view_spending_patterns()
        elif choice == "3":
            total_spending = tracker.get_total_spending()
            print("---------Your Total Spending Amount----------")
            print(f"Total Spending: {total_spending}/-")
            print("----------------------------------------")
        elif choice == "4":
            date_input = input("Enter date to view expenses (YYYY-MM-DD): ")
            expense_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            print("---------View Expenses by Date----------")
            tracker.view_expenses_by_date(expense_date)
            print("----------------------------------------")
        elif choice == "5":
            print("Exiting...thank you, see you soon :)")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
