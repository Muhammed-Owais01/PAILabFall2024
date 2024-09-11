class Account:
    def __init__(self, acc_num, acc_bal, sec_code):
        self.__account_no = acc_num
        self.__account_bal = acc_bal
        self.__security_code = sec_code

    def display_account_data(self):
        print(f"Account No: {self.__account_no}, Account Balance: {self.__account_bal}, Security Code: {self.__security_code}")

obj1 = Account(19312, 3333, 1023921)
obj1.display_account_data()