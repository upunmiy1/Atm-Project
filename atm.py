# Intitialization Code
Pin = 1234        
Starting_balance = 10000
twenty = 0
ten = 0
five = 0
Pin_entry = int(input("Enter the PIN: "))  #Takes the input from user for pin

#Main Code
if Pin_entry == Pin:
    print("Correct:\n")
    
    Withdraw = int(input("Enter the amount to withdraw:")) #takes the input from user for money to witghdraw
    
    if Withdraw <= Starting_balance:
        twenty = int(Withdraw/20)
        x = int(Withdraw%20)             #gives the remainder for the rest of money after being divided by 20
        ten = int(x/10)              
        y = int(x%10)                    #gives the remainder after being divided by 10
        five = int(y/5)
        print("Transaction Successful, Number of 20 bills:", twenty)
        print("Transaction Successful, Number of 10 bills:", ten)
        print("Transaction Successful, Number of 5 bills:", five)
        
        
    else:
        K = str(input("Current entry is more than the balance in atm, Do you want to proceed, You might be charged?\n (YES/NO): "))                #takes input from user inorder to move ahead
        
        if(K == 'YES' or K=='yes'):
            print("You have been charged with penalty for: 20 $")
        else:
            print("Returning to the main Window.")
        
else:
    print("Incorrect PIN")
