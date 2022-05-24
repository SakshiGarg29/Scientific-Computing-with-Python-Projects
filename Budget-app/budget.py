class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.amount = 0


    def __str__(self):
        s = self.category.center(30, "*") + "\n"
        for transaction in self.ledger:
            amount = 0
            description = ""
            for key, value in transaction.items():
                if key == "amount":
                    amount = value
                elif key == "description":
                    description = value
            if len(description)> 23:
                description = description[:23]
            amount = str(format(float(amount),'.2f'))
            if len(amount)>7:
                amount = amount[:7]
            s += description +str(amount).rjust(30-len(description)+"\n")
        s += "Total: " + str(format(float(self.amount),'.2f'))
        return s


    def check_funds(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

    # A deposit method that accepts an amount and description
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount,"description": description})
        self.amount += amount

    # A withdraw method that is similar to the deposit method,
    # but the amount passed in should be stored in the ledger as a negative number
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    # A get_balance method that returns the current balance
    def get_balance(self):
        return self.amount

    # A transfer method that accepts an amount and another budget category as arguments
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount": -amount, "description" :"Transfer to" + category.category})
            category.ledger.append({"amount": amount, "description" :"Transfer from " + self.category })
            return True
        else:
            return False

    def create_spend_chart(categories):
        spend = []
        for category in categories:
            temp = 0
            for item in category.ledger:
                if item['amount'] < 0:
                    temp += abs(item['amount'])
            spend.append(temp)

        total = sum(spend)
        percentage = [i/total * 100 for i in spend]

        s = "Percentage spent by category"
        for i in range(100, -1, -10):
            s += "\n" + str(i).rjust(3) + "|"
            for j in percentage:
                if j > i:
                    s+= " o "
                else:
                    s += "  "
            # Spaces
            s += " "
        s += "\n    ----------"

        cat_length = []
        for category in categories:
            cat_length.append(len(category.category))
        max_length = max(cat_length)

        for i in range(max_length):
            s += "\n   "
            for j in range(len(categories)):
                if i < cat_length[j]:
                    s += " " + categories[j].category[i] + " "
                else:
                    s += "   "
        # Spaces
        s += " "
        return s
