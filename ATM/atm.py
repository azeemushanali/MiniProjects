class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()

        

    def menu(self):
        statement = """
        Hello, How would you like to procees?
        Enter your choice>>>
        1. Enter 1. to create PIN 
        2. Enter 2. to DEPOSIT
        3. Enter 3. to WITHDRAW
        4. Enter 4. to CHECK BALANCE
        5. Enter 5. to EXIT
        """
        while(True):
            user_input = input(statement)
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit()
            elif user_input=="3":
                self.withdraw()
            elif user_input=="4":
                self.check_balance()
            elif user_input=='5':
                print("BYE!!!")
                exit()
            else:
                print("BYE!!!")
    def check_pin(self):
        if self.pin=="":
            print("Please create pin first")
            self.menu()

    def create_pin(self):
        self.pin=input("Enter your PIN>>> ")
        print("PIN created successfully")

    def deposit(self):
        self.check_pin()
        temp = input("Enter your PIN>>> ")
        if temp==self.pin:
            amount=int(input("Enter your amount to deposit>>> "))
            self.balance = self.balance+amount
            print(f"Deposit of amount {amount} is done!!! Your new account balance is {self.balance}")
        else:
            print("PIN is incorrect, try again")

            

    def withdraw(self):
        self.check_pin()
        temp = input("Enter your PIN>>> ")
        if temp==self.pin:
            amount=int(input("Enter the amount to withdraw >>> "))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print(f"Collect your ${amount} money, Your remaining balance is {self.balance}")
            else:
                print("Insufficient funds")
        else:
            print("PIN incorrect, try again")

    def check_balance(self):
        temp = input("Enter your PIN>>> ")
        if temp==self.pin:
            print("Hi,Your account balance is - " , self.balance)
        else:
            print("PIN is incorrect, try again")

 

customer1 = Atm()
