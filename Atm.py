import time
# to enter the atm card
print("Please insert your card:")
#  wait for some time to enter the atm pin number
time.sleep(5)
password= 4567
pin = int(input ("Enter your pin"))
balance = 10000
while True:
  if password == pin:    # for checking the already set pin and enter current time pin number
    print(""" please enter your choice :
              1. Balance
              2. Withdraw amount 
              3. Deposite Balance 
              4. Exit """)
     
     # to choose any option from the above options according to your chioce

    try:
      option = int(input("Enter your choice:"))
      
    except:
      print("Please enter the valid choice")

     # for checking the balance 
    if option == 1:
      print(f"Your current balance is {balance}")
      
    # for withdraw the amount from the current balance and also show the current balance
    if option == 2:
      withdraw_amount = int(input("Please enter withdraw amount:"))
      balance = balance - withdraw_amount
      print(f"{withdraw_amount} is debited from your account")
      print(f"Your current balance is {balance}")

    # for deposite the amount in your account and also check the current balance
    if option == 3:
      deposite_amount = int(input("Please enter withdraw amount:"))
      balance = balance + deposite_amount
      print(f"{deposite_amount} is credited to your account")
      print(f"Your current balance is {balance}")
    
    # for exit
    if option == 4:
      break
else:
    print("please enter the valid pin number")