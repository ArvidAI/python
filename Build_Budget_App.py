class Category:
    """Represents a budget category (e.g. Food, Clothing, Auto) that
    tracks a ledger of deposits and withdrawals."""

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Add a deposit to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Add a withdrawal to the ledger if there are sufficient funds.
        Returns True if the withdrawal took place, False otherwise."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Return the current balance of the category based on deposits
        and withdrawals in the ledger."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        """Withdraw an amount from this category and deposit it into
        another Category instance. Returns True if the transfer took
        place, False otherwise."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Return False if amount is greater than the current balance,
        otherwise return True."""
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])[:7]
            line = description + amount.rjust(30 - len(description))
            items += line + "\n"
        total = "Total: {:.2f}".format(self.get_balance())
        return title + items + total


def create_spend_chart(categories):
    """Given a list of Category objects, return a string that is a bar
    chart showing the percentage spent by category, rounded down to the
    nearest 10."""
    title = "Percentage spent by category\n"

    # Calculate total spent (withdrawals only) per category
    spent_amounts = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    if total_spent == 0:
        percentages = [0 for _ in spent_amounts]
    else:
        percentages = [
            int((spent / total_spent) * 100) // 10 * 10 for spent in spent_amounts
        ]

    # Build the horizontal bars, 100 down to 0 in steps of 10
    chart = ""
    for value in range(100, -1, -10):
        chart += str(value).rjust(3) + "|"
        for percentage in percentages:
            chart += " o " if percentage >= value else "   "
        chart += " \n"

    # Dashed line beneath the bars
    dashes = "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Build the rotated category name labels beneath the dashes
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
    label_lines = ""
    for i in range(max_len):
        label_lines += "    "
        for name in names:
            char = name[i] if i < len(name) else " "
            label_lines += " " + char + " "
        label_lines += " \n"

    return (title + chart + dashes + label_lines).rstrip("\n")

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)