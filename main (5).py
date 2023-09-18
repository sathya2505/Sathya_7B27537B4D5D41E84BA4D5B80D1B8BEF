class BankAccount:

 def _init_(self,account_number, account_holder_name,initial_balance = 0.0):
  self.__account_number = account_number
  self.__account_holder_name = account_holder_name
  self.__account_balance = initial_balance

 def deposit(self,amount):
   if amount > 0:
    self.__account_balance += amount
    print("Deposited ₹{}. New balance: ₹{}".format(amount,self.__account_balance)) 
   else:
    print("Invalid deposit amount.")

 def withdraw(self,amount):
   if amount > 0 and amount <=  self.__account__balance:
    self.__account_balance -= amount
    print("withdraw ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
   else:
    print("Invalid withdrawal amount.")
 def display_balance(self):
  print("Account balance for{}.") 
        
class Player:

 def play (self):
  print("The player is playing cricket.")

class Batsman:
 def play (self):
  print ("The Batsman is batting") 

class Bowler:
 def play (self):
  print ("The Bowler is bowling") 

Batsman = Batsman() 
Bowler = Bowler() 

Batsman. play() 
Bowler. play()  
