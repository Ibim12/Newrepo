
import random

class Account_number:
    def __init__(self):
        print('Inside Constructor')
        print('All variables initialized')
    def account_number_generation(self):
        account_numb = []
        acc_no=account_numb
        for i in range(0,7):
            n = random.randint(0,9)
            account_numb.append(n)
        account_number=''.join(str(e) for e in acc_no)
        account_number1=f'020{account_number}'
        return account_number1
# ac_no= Account_number()
# print(ac_no.account_number_generation())         

account_number_db=set()


account_number_db.add(Account_number)
# 
# # print(len(account_number_db))