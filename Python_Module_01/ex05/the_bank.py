class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

        def transfer(self, amount):
            self.value += amount


class Bank(object):

    """The bank"""

    def __init__(self):

        self.accounts = []

    def __verify(self, account):
        if len(account.__dict__) % 2 == 0:
            return False

        for key, value in account.__dict__.items():
            if key[0] == 'b':
                return False

        if not any(key.startswith('zip') or key.startswith('addr')
                   for key, value in account.__dict__.items()):
            return False

        if not {'name', 'id', 'value'}.issubset(account.__dict__.keys()):
            return False

        if not (isinstance(account.__dict__['name'], str) and
                isinstance(account.__dict__['id'], int) and
                isinstance(account.__dict__['value'], float)
                ):
            return False

        if any(account == item for item in self.accounts):
            return False

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if self.__verify(new_account) is False:
            return False

        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if amount < 0:
            return False
        if origin.__dict__['value'] < amount:
            return False
        if not (self.__verify(origin) and self.__verify(dest)):
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        # ... Your code ...


if __name__ == "__main__":
    print("hello world")
    a = Bank()
    b = Account("a")
    print(b.__dict__)
    a.add(b)
    print(a.accounts)

    c = Account("a")
    del c.__dict__['id']
    print(c.__dict__)
    a.add(c)
    print(a.accounts)

    d = Account("d", zipcode=111, addr="aaa", value=1.2)
    # d.__dict__['id'] = 1.1
    print(d.__dict__)
    a.add(d)
    print(a.accounts)

    a.add(d)
    print(a.accounts)
