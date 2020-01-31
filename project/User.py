class User:
    amount_of_users = 0

    def __init__(self, username, starting_balance):
        self.username = username
        self.balance = starting_balance
        User.amount_of_users += 1
        self.your_number_in_line = User.amount_of_users - 1

    def receive_money(self, amount):
        int_amount = int(amount)
        self.balance += int_amount

    def send_money(self, amount):
        int_amount = int(amount)
        self.balance -= int_amount
        return int_amount

    def get_balance(self):
        return self.balance

    def get_username(self):
        return self.username

    def get_line_number(self):
        return self.your_number_in_line

    # Returns 1 if balance is good, returns 0 if there would an overdraft
    def check_balance(self, amount):
        if int(amount) <= self.balance:
            return 1
        else:
            return 0
