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

    def __security_check(self, account):
        if len(account.__dict__) % 2 == 0:
            print("account with even number attribute is--corrupted")
            return False

        for key, value in account.__dict__.items():
            if key[0] == 'b':
                print("beginning of name of key cannot be start with b--corrupted")
                return False

        if not any(key.startswith('zip') or key.startswith('addr')
                   for key, value in account.__dict__.items()):
            print("account with no zip or addr is--corrupted")
            return False

        if not {'name', 'id', 'value'}.issubset(account.__dict__.keys()):
            print("account with no 'name', 'id', 'value' is--corrupted")
            return False

        if not (isinstance(account.__dict__['name'], str) and
                isinstance(account.__dict__['id'], int) and (
                    isinstance(account.__dict__['value'], float) or
                    isinstance(account.__dict__['value'], int))
                ):
            return False

        return True

    def __search_by_name(self, name) -> Account:
        for account in self.accounts:
            if account.__dict__['name'] == name:
                return account
        return None

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if not isinstance(new_account, Account):
            return False
        print("1", new_account.__dict__['name'])
        if any(new_account.__dict__['name'] == item.__dict__['name']
                for item in self.accounts):
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if amount < 0:
            print("amount to transfer is less than 0")
            return False
        if (origin == dest):
            return True
        origin_account = self.__search_by_name(origin)
        if origin_account is None:
            print("Account not found for:", origin)
            return False
        dest_account = self.__search_by_name(dest)
        if dest_account is None:
            print("Account not found for:", dest)
            return False
        if not self.__security_check(origin_account):
            print("Verification for account", origin_account.name, "failed")
            return False
        if not self.__security_check(dest_account):
            print("Verification for account", dest_account.name, "failed")
            return False
        if origin_account['amount'] < amount:
            print("insufficient amount for origin account.")
            return False
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        if self.__search_by_name(name) is None:
            return False

        target_account = self.__search_by_name(name)


        # for key, value in target_account.__dict__.items():
        #     if value is None:
        #         del target_account.__dict__[key]

        print(self.__search_by_name(name).__dict__)


if __name__ == "__main__":
    print("hello world")
    the_bank = Bank()
    a = Account("a")
    print(the_bank.__dict__)
    the_bank.add(a)
    print(the_bank.accounts)

    aa = Account("a")
    del aa.__dict__['id']
    print(aa.__dict__)
    the_bank.add(aa)
    print(the_bank.accounts)

    c = Account("c", zipcode=111, addr="aaa", value=1.2)
    # d.__dict__['id'] = 1.1
    print(c.__dict__)
    the_bank.add(c)
    print(the_bank.accounts)

    the_bank.add(c)
    print(the_bank.accounts)
