class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_number: str, owner: str, initial_balance: float):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być wieksza od zera")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Kwota wyplaty musi być większa niz zero")
        if self.balance < amount:
            raise InsufficientFundsError("Za mało środków")
        self.balance -= amount

    async def transfer(self, to_account, amount: float):
        if amount <= 0:
            raise ValueError("Kwota przelewu musi być większa od zera")
        if self.balance < amount:
            raise InsufficientFundsError("Niewystarczające środki na koncie")
        self.balance -= amount
        to_account.deposit(amount)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float):
        if account_number in self.accounts:
            raise ValueError("Konto o tyn numerze już istnieje")
        if initial_balance < 0:
            raise ValueError("Saldo początkowe nie może być ujemne")
        self.accounts[account_number] = Account(account_number, owner, initial_balance)

    def get_account(self, account_number: str):
        if account_number not in self.accounts:
            raise ValueError("Nie znaleziono konta o takim numerze")
        return self.accounts[account_number]

    async def process_transaction(self, transaction_func):
        await transaction_func()
