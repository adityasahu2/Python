class Accounts:
    bankName = "ABC Bank"
    def __init__(self, name, accNo, balance):
        self.name = name
        self.accNo = accNo
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Name: {self.name}\nDeposited: {amount}\nBalance: {self.balance}\n")

    def withdraw(self,amount):
        if self.balance > 0 and amount < self.balance:
            self.balance -= amount
            print(f"Name: {self.name}\nWithdraw: {amount}\nBalance: {self.balance}\n")
        else:
            print("Low Balance")

    def display(self):
        print("Bank Name: "+ self.bankName,"\nName:",self.name,"\nAccount No.:",self.accNo,"\nBalance:",self.balance,"\n")

acc1 = Accounts("Aditya", 1, 10000)
acc2 = Accounts("Lipsa", 2, 30000)
acc3 = Accounts("Bhagyashree", 3, 20000)

acc1.display()
acc2.display()
acc3.display()

acc1.deposit(10000)
acc1.withdraw(15000)

print("Aditya"+"Lipsa") #Concat
print("Aditya","Lipsa") #Separate