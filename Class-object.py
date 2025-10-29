class BankAccount:
    def __init__(self,Accountno,Accountholdername,balance):
        self.Accountno=Accountno          #public attribute
        self.Accountholdername=Accountholdername  #public attribute
        self.__balance=balance            #private attribute
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance.")                
        else:
            self.__balance-=amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
    def get_balance(self,Accountno):
        if Accountno==self.Accountno:
            return self.__balance
        else:
            return "Invalid Account Number."
# Creating object of BankAccount
account1=BankAccount("123456","John Doe",1000)  
account1.deposit(500)          # Depositing money
account1.withdraw(200)         # Withdrawing money  
print("Current Balance:",account1.get_balance("1234567"))  # Getting balance with correct account number
        
        