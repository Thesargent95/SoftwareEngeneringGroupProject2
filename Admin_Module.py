class Admin_Module:

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def new_ATM_Card(accnt_num, pin, account_name, date_of_issue, exp_date, address, balance):
        pass

    def view_ATM_Status():
        pass

    def update_ATM_Card(action):
        "Perameter 'action' is a suggestion"
        pass


class ATM_Card:
    def __init__(self, accnt_num, pin, account_name, date_of_issue, exp_date, address, balance):
        super(, self).__init__()
        self.accnt_num = accnt_num
        self.account_name = account_name
        self.pin = pin
        self.date_of_issue = date_of_issue
        self.exp_date = exp_date
        self.address = address
        self.balance = balance

class Account:
    "Insert array or list here for ATM Cards"
        def __init__(self, arg):
    super(, self).__init__()
            self.arg = arg
