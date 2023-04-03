# TODO: fix fix_account function in progress
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

    def check_corrupted(self):
        if not hasattr(self, 'value'):
            raise AttributeError("the 'value' Attribute does not exist.")

        if len(self.__dict__) % 2 == 0:
            print("account with even number attribute is--corrupted")
            return False

        for key, value in self.__dict__.items():
            if key[0] == 'b':
                print("beginning of name of key cannot be start with b--corrupted")
                return False

        if not any(key.startswith('zip') or key.startswith('addr')
                   for key, value in self.__dict__.items()):
            print("account with no zip or addr is--corrupted")
            return False

        if not {'name', 'id', 'value'}.issubset(self.__dict__.keys()):
            print("account with no 'name', 'id', 'value' is--corrupted")
            return False

        if not (isinstance(self.__dict__['name'], str) and
                isinstance(self.__dict__['id'], int) and (
                    isinstance(self.__dict__['value'], float) or
                    isinstance(self.__dict__['value'], int))
                ):
            return False

        return True



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
        print(name)
        for account in self.accounts:
            print(account.__dict__['name'])
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
        if origin_account.__dict__['value'] < amount:
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
            print("Error: name is not an instance of str")
            return False
        if self.__search_by_name(name) is None:
            print("Error: name not found")
            return False

        target_account = self.__search_by_name(name)

        filtered = {k: v for k, v in target_account.__dict__.items()
                    if v is not None}
        target_account.__dict__.clear()
        target_account.__dict__.update(filtered)

        keys_to_delete = []
        for key, value in target_account.__dict__.items():
            if key[0] == 'b':
                print(key)
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del target_account.__dict__[key]


        if not any(key.startswith('zip') or key.startswith('addr')
                   for key, value in target_account.__dict__.items()):
            return False

        if not {'name', 'id', 'value'}.issubset(target_account.__dict__.keys()):
            return False

        try:
            target_account.__dict__['name'] = str(
                target_account.__dict__['name'])
        except:
            return False

        try:
            target_account.__dict__['id'] = id(target_account.__dict__['id'])
        except:
            return False

        if len(target_account.__dict__) % 2 == 0:
            target_account.odd_maker = True

        return True


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


    # bank = Bank()
    # john = Account(
    #     'William John',
    #     zip='100-064',
    #     brother="heyhey",
    #     value=6460.0,
    #     ref='58ba2b9954cd278eda8a84147ca73c87',
    #     info=None,
    #     other='This is the vice president of the corporation',
    #     lol="hihi"
    # )
    # print(john.__dict__)
    # bank.add(john)
    # print("before", john.check_corrupted())
    # print("fix", bank.fix_account("William John"))
    # print(john.__dict__)
    # print("after", john.check_corrupted())
    # print(type(john.__dict__['name']))
    # print(type(john.__dict__['id']))
    # print(type(john.__dict__['value']))

    # john = Account(
    #     'William John',
    #     zip='100-064',
    #     rother="heyhey",
    #     value=6460.0,
    #     ref='58ba2b9954cd278eda8a84147ca73c87',
    #     info=None,
    #     other='This is the vice president of the corporation',
    # )

    # print("corrupted:", john.check_corrupted())
    # print(bank.fix_account("William John"))

    # john = Account(
    #     'William John',
    #     zip='100-064',
    #     rother="heyhey",
    #     ref='58ba2b9954cd278eda8a84147ca73c87',
    #     info=None,
    #     other='This is the vice president of the corporation',
    #     lol = "lolilol"
    # )

    # print(john.__dict__)
    # print("check:", john.check_corrupted())

    # # bank.add(john)

    # # print(bank.fix_account("William John"))
    # # print("check:", john.check_corrupted())

    # print("-------------------")
    # bank.add(
    # Account(
    #     'Jane',
    #     zip='911-745',
    #     value=1000.0,
    #     ref='1044618427ff2782f0bbece0abd05f31'
    #     )
    # )

    # jhon = Account(
    #     'Jhon',
    #     zip='911-745',
    #     value=1000.0,
    #     ref='1044618427ff2782f0bbece0abd05f31'
    # )

    # bank.add(jhon)

    # print("testing a valid transfer")
    # print(jhon.value)
    # bank.transfer("Jane", "Jhon", 500)
    # print(jhon.value)

    # bank.transfer("Jane", "Jhon", 1000)
    # print(jhon.value)




