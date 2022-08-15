from multiprocessing import current_process
from sunau import AUDIO_FILE_ENCODING_MULAW_8
from unicodedata import name

savings_interest=0.014
fixed_depo_interest=0.015
interest= capital*interest
capital=int("capitals")
def capitals_with_interest:
    capital+interest
# class Bank:

#     kind = 'Account'         # class variable shared by all instances

#     def __init__(self,name,capital,interest,returns,loss,fees):
#         self.name = "Current_Account"
#         self.capital = capital
#         self.rate = None
#         self.interest= None   
#         self.loss= "card fees"
#         self.fees= "withdrawals"
#         self.returns = None

#     def __init(self,name,capital,interest,loss,fees):
#         self.name = "Savings Account"
#         self.capital = capital
#         self.interest = 1.4
#         self.rate = "Monthly"
#         self.loss = None
#         self.returns = capitalswithinterest()
#         self.fees = None

#     def __init(self,name,capital,interest,loss,fees):
#         self.name = "Fixed Deposit Account"
#         self.capital= capital
#         self.interest= 1.5
#         self.rate= "Six-Month"
#         self.loss = None
#         self.returns = capitalswithinterest
        # self.fees = None
# class SBank:
#     def __init__(self,name) :
#         self.name=name
#     def get_name(self):
#         return self.name


# class Goat:
#     def __init__(self,name) -> None:
#         self.name=name
#     def get_goat_name(self):
#         return self.name
#  class YBank(SBank):
#      def __init__(self,name) -> None:
#          self.goat=Goat()
    
#      def get_name_of_goat(self):
#         return self.goat.get_goat_name()

# ybank=YBank('Kingsley')
# print(ybank.get_name())

# class per_of_returns_per_annum:
#     def__init__(self,name) -> None:
#         self.name= name
#     def get_period(self):
        

# class interest_rates:
#     def__init__(self,name) -> None:
#         self.name=name
#     def get_interest_rate(self):

class Bank:
    def __init__(self,name,capitals_with_interest) :
        self.name=name
    def get_name(self):
        return self.name
    def returns_account(self):
        return capital

class Savings_Account(Bank):
    # def __init__(self,name) -> None:
    #     self.goat=Goat()
    
    def get_name(self):
        return self.name

class Fixed_Deposit_Account(Bank):
    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        return self.name

class Current_Account(Bank):
    def __init__(self,name):
        super().__init__(name)

        def get_name(self):
            return self.name

savings=Fixed_Deposit_Account('baba')
print(savings.name)