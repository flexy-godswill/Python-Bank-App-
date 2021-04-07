#i imported the time module
import time

# Created all account using a list
users = ["Parrot", "Bell", "Cynthialu"]
password =["parrotos", "bella's butter", "cynthia"]
group = ["admin", "Mentor", "Intern"]
mail = []
    

#creating a validation for my form
def validate(form):
    if len(form) > 0:
        return False
    return True

# I Created an authorization for my login
def Loginauth(username, password):
    if username in users:
        if password ==["password"]:
            print("Your Login Was Successful")
            return True
        return False

# Login
def Login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username invalid")
        else:
            break
        
    while True:
        password = input("Enter Your Password: ")
        if not len(password) > 0:
            print("Password Invalid")
        else:
            break

    if Loginauth (username, password):
        return session (username)
    else:
        print("Invalid Username Or Password")


#Register
def Register():
    while True:
        username = input("Enter A New Username")
        username.append(users)
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
        while True:
            password = input("Enter A New Password")
            password.append(password)
            if not len(password) > 0:
                print("Password can't be blank")
                continue
            else:
                break

        print("Creating Your Acount....Please Give Us A Min...")
        users[username] = {}
        users[username]["password"] = password
        users[username]["group"] = "user"
        users[username]["mail"] = []
        time.sleep(3)
        print("Account Has Been Created")

#Send An E-mail
def sendmail (username):
    while True:
        recipient = input("Recipient > ")
        if not len(recipient) > 0:
            print("Recipient Can't Be Blank")
            continue
        elif recipient not in users:
            print("There is no account with that username")
            continue
        else:
            break
    while True:
        subject = input("Subject Of Your E-mail > ")
        if not len(subject) > 0:
            print("Subject Can't Be Blank")
            continue
        else:
            break
        
    while True:
        context = input("Context Of Your E-mail")
        if not len(context) > 0:
            print("Context Can't Be Blank")
        else:
                break
        print("Sending Mail....")
        users[recipient]["mail"].append(["Sender: " + username, "subject: " + subject, "Context: " + context])
        time.sleep(3)
        print("Mail Has Been Sent To " + recipient)

#User Session
def session(username):
    print("Welcome To Your Account " + username)
    print("Options: View Mail | Send Mail | Log Out")
    if users[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ")
        if option == "Log Out":
            print("Logging Out..........")
            break
        elif option == "View Mail":
            print("Current Mail")
            for mail in users[username]["mail"]:
                print(mail)
        elif option == "Send Mail":
            sendmail(username)
        elif users[username]["group"] == "admin":
            if option == "user mail":
                print("Whose Mail Would You Like To See?")
                userinfo = input("> ")
                if userinfo in users:
                    for mail in users[userinfo]["mail"]:
                        print(mail)
                else:
                    print("There Is No Account With That Username")
            elif option == "delete mail":
                print ("Whose Mail Would You Like To Delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Deleting " + userinfo + "'s Mail.....")
                    users[userinfo]["mail"] = []
                    time.sleep(3)
                    print(userinfo + "'s Mail Has Been Deleted")
                else:
                    print("There Is No Account WIth That Username")
            elif option == "delete account":
                print("Whose Account Would You Like To Delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Are You Sure You Want To Delete " + userinfo + "'s Account?")
                    print("Options: Yes } No")
                    while True:
                        confirm = input("> ")
                        if confirm == "Yes":
                            print("Deleting " + userinfo + "'s Account......")
                            del users[userinfo]
                            time.sleep(3)
                            print(userinfo + "'s Account Has Been Deleted")
                            break
                        elif confirm =="No":
                            print("Cancelling Account Termination........")
                            time.sleep(2)
                            print("Account Termination Cancelled")
                            break
                        else:
                            print(confirm + " Is Not An Option")
                else:
                    print("There Is No Account With That Username")
        else:
            print(option + " is not an option")


# On Start
print("Welcome To The System. Please Register Or Login.")
print("Options: Register | Login | Exit")
while True:
    option = input("> ")
    if option == "Login":
        Login()
    elif option == "Register":
        Register()
    elif option == "Exit":
        break
    else:
        print(option + " Is Not An Option")


#On Exit
print("Shutting Down.......")
time.sleep(2)





        
                
                      
