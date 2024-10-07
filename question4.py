1#  WITI Academy is proposing a Sacco to help students save their money. 
#  Design a platform that will do the following.
#  Welcome to, WITIAcademy Sacco.
#  1. Deposit Money
#  2. Withdraw Money
#  3. Check Balance
#  Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#  If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
#  If the student selects 3, the account balance should be displayed.

#Answer4

def witi_academy_sacco():
    
    AccountBalance = 0
    run = 1
    
    while run == 1:
        
    
        print("\nWelcome to, WITIAcademy Sacco:")
        
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        
        option =int(input("Enter the option (1,2,3): "))
        
        
        
        if option == 1:
            print("Transaction in process:.....")
            deposit_amount = int(input("Enter the amount to Deposit: "))
            #if deposit_amount == 1000:
            #    print("Amount Deposited")
            if deposit_amount < 1000:
                print("The minimum depsoit should be 1000! \n Please try again")
            else:
                AccountBalance += deposit_amount
                print(f"Dear student, you have deposited {deposit_amount:,} and your updated account balance is {AccountBalance} ")
            
            
            
        
        elif option == 2:
            print("Your Transaction is in progress!......")
            amount_to_be_withdrawn = int(input("Enter the Amount to be withdrawn: "))
            
            if AccountBalance == 0:
                print("Sorry!, your balance is 0")
            elif AccountBalance < 500:
                print("Sorry!, the least amount to be withdrawn is 500, please renter")
            elif amount_to_be_withdrawn > AccountBalance:
                print("Sorry you have insufficent funds, Withdraw failed!")
            else:
                AccountBalance -= amount_to_be_withdrawn
                print(f"Dear student, you have withdrawn {amount_to_be_withdrawn:} and your new account balance is {AccountBalance:}")
        
        
        
        elif option ==3:
            print("Your account balance is loading.......")
            print(f"Your Account Balance is {AccountBalance:, }")
        
        
        else:
            print("Please Enter either 1,2 0r 3! \n")
            
    run = int(input("Enter 1 to continue and 5 to exit the transaction: "))
    
    if run !=1:
        print("Transaction has ended, Thanks for using the Sacco ")
        
        
    witi_academy_sacco()
        
    
