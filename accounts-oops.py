import datetime
import pytz


class Account:
    """Simple account class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize((utc_time))
    def __init__(self,name,balance,):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(),balance)]
        print("account created for "+ self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount should be greater than zero and no more than account balance")
        self.show_balance()
    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date,amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1

            print("{:6} {} on {} (local time was {})".format(amount,tran_type,date,date.astimezone()))

if __name__ == '__main__':
    sreekar = Account("Sreekar",0)
    sreekar.show_balance()

    sreekar.deposit(1000)
    #sreekar.show_balance()

    sreekar.withdraw(500)
    #sreekar.show_balance()

    sreekar.withdraw(2000)
    sreekar.show_transactions()


    praveen = Account("praveen",800)
    praveen.__balance=200
    praveen.deposit(100)
    praveen.withdraw(200)
    praveen.show_transactions()
    praveen.show_balance()

