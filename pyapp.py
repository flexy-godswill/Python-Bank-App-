from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S:%p")

name = input("What is your name? \n")
allowedUsers = ['Jenyfa', 'Folababy', 'Kess']
allowedPin = ['0123', '4567', '8910']
accountBalance = [15000, 13000, 11000]

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPin[userId]):
       print('Welcome %s' % name)

       print(dt_string)
       print('These are the available options:')
       print('1. Withdrawal')
       print('2. Cash Deposit')
       print('3. Complaint')
       print('4. View Balance')

       selectedOption = int(input('Please select an option:'))

       if(selectedOption == 1):
           print('1. Savings')
           print('2. Current')
           saving = int(input("Select Account Type"))
           
           if saving == 1:
               print('1. 1000')
               print('2. 2000')
               print('3. 5000')
               print('4. Other')

           withdraw = int(input("How Much Do You Want To Withdraw? \n"))
           if withdraw == 4:
               prin = int(input("Enter Amount.. \n"))
           if withdraw > accountBalance[userId]:
               print('Insufficient Funds, Will You Like To Try Something Else?')
           if withdraw < accountBalance[userId]:
               print('Transaction Successful, Please Take Your Cash,Would You Like To Make Another Transaction? \n')
           print('1. Yes')
           print('2. No')
           selectOption = int(input('Please Select An Option:'))

           if (selectOption == 1):
                print('Enter Your Pin Again To Continue')
           elif(selectOption == 2):
        
               print('Please Take Your Card')
                                

           
           
       elif(selectedOption == 2):
           print('You selected %s' % selectedOption)
           howMuch = int(input('How Much Do You Wish To Deposit?'))
           currBal = accountBalance[userId] + howMuch
           print("Deposit Successful, Thanks For Banking With us...Your New Account Balance is %s" % currBal)

           
       elif(selectedOption ==3):
           print('You selected %s' % selectedOption)
           messageBox = input ('Enter Your Complaint.... \n')
           print('We Have |Received Your Complaint, Thanks For Contacting Us....')

       elif(selectedOption ==4):
           print('Your Account Balance is', accountBalance[userId])

       else:
           print('Invalid Option selected, please try again')
              
    else:
       print('Password Incorrect, please try again')
        
else:
    print('Name not found, please try again')
















