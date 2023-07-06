#----------------------------------------------------------------------------------------------------------------------------------------------#
#Collaborator(s):Ehiane Kelvin Oigiagbe and Chat-GPT                                                                                           #
#Description:  ---------------------------------[BANKING SYSTEM]-------------------------------------------------------------------------------#
        # This program mimicks a basic banking system that enables both existing and new users to access and manage their accounts. -----------#
        # The program verifies user information and stores it in a file, giving users the option to log in or create a new user account. ------#
        #Existing users can log in by providing their name and the last four digits of their routing number.-----------------------------------#
        #Once the information is authenticated, the user gains access to their account.--------------------------------------------------------#
        #New users are prompted to enter their personal details, which the program verifies before displaying their account balances.----------#
        #Users can then distribute their balance among their accounts before their information is saved to a file.-----------------------------#
        #The code features a loading animation that displays a message while the program executes various tasks.-------------------------------#
        #It also uses the User and Bank classes to store and manipulate user and account information.------------------------------------------#
        #The Bank class contains functions for logging in, displaying account balances, and saving user information to a file. ----------------#
        #Overall, the code presents a simple yet functional banking system that enables users to create and manage their accounts securely.----#
#Start Date: [14th March 2023]-----------------------------------------------------------------------------------------------------------------#                                                                                                                    
#End Date: [16th March 2023] --> 2:19pm---------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#

#IMPORT(S)
import random
import string 
import time

#PROGRAM CONSTANTS
DEFAULT_ACCOUNT_TYPE = "Checking account";
DEFAULT_ROUTING_NUMBER = "00000000000"; 
DEFAULT_ACCOUNT_NUMBER = "0000000000000"; 
SIZE_OF_ROUTING_NUMBER = 10;
SIZE_OF_ACCOUNT_NUMBER = 13;
MAX_NUMBER_OF_ACCOUNTS = 2;
DEFAULT_STRING = "";
DEFAULT_INT = 0;
DEFAULT_FLOAT = 0.00;
EXISTING_USER = 1;
NEW_USER = 2;

#creating parent class: User;
class User:
    #private members:
    def __init__(self,name,age,gender,numberOfAccounts,balance = 0.00):
        self.name = name;
        self.age = age;
        self.gender = gender;
        self.numberOfAccounts = numberOfAccounts;
        self.balance = balance;
    
    def __deposit__(self,newAmount):
        self.balance += newAmount;
        print(f"\nYou have just deposited ${newAmount};\nYour total balance is ${self.balance}");


    def ___withdraw__(self,amountTaken):
        self.balance -= amountTaken;
        print(f"\nYour new total balance is ${self.balance}");


    #public memebers:
    def confirm_deposit(self,newAmount):
        self.__deposit__(newAmount);    

    def confirm_withdrawal(self,amountTaken):
        self.___withdraw__(amountTaken);
    
    def viewAccountBalance(self):
        print(f"\nPrinting account info:\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}\nNumber Of Accounts: {self.numberOfAccounts}\nCurrent Balance: {self.balance}");

    def getUserInfo(self):
        userName = input("Enter User's name here: ");
        userAge = int(input(f"Enter {userName}'s age here: "));
        userGender = input(f"Enter {userName}'s  gender here: ");
        num_of_acct = int(input(f"How many accounts does the {userName}'s wish to have[Note: MAX = {MAX_NUMBER_OF_ACCOUNTS}]: "));
        curr_balance = float(input(f"What starting amount does {userName}'s want to deposit: $"));
        self.name = userName;
        self.age = userAge;
        self.gender = userGender;
        self.numberOfAccounts = num_of_acct;
        self.balance = curr_balance;
        print("****\n!Successfully Stored User's Info Data!\n****")

   
class Bank(User):
    #private members:
    def __init__(self,User,routingNumber=DEFAULT_ROUTING_NUMBER,accountNumber=DEFAULT_ACCOUNT_NUMBER,checking_balance = 0.00,savings_balance = 0.00, checking_routing_number = DEFAULT_ROUTING_NUMBER,savings_routing_number = DEFAULT_ROUTING_NUMBER, checking_account_number = DEFAULT_ACCOUNT_NUMBER, savings_account_number = DEFAULT_ACCOUNT_NUMBER):
        super().__init__(User.name, User.age,User.gender,User.numberOfAccounts,User.balance);
        self.routingNumber = routingNumber;
        self.accountNumber = accountNumber;
        self.checking_balance = checking_balance;
        self.savings_balance = savings_balance;
        self.checking_routing_number= checking_routing_number
        self.checking_account_number = checking_account_number
        self.savings_routing_number = savings_routing_number 
        self.savings_account_number = savings_account_number
        #creating class Dictionary:
        self.classDict = {User.name:[routingNumber,accountNumber]}; #i'll add intrest rate later.


    def __generateRoutingNumber__(self):
        tempRN = "";
        for i in range(SIZE_OF_ROUTING_NUMBER):
            currentCharacter = random.choice(string.ascii_uppercase + string.digits);  #generates a random character that is either a AN uppercase letter or number
            tempRN += currentCharacter;
    
        if tempRN == "":
            tempRN = DEFAULT_ROUTING_NUMBER;
            print("----![Routing]Operation Failed!-----");
        self.routingNumber = tempRN;
        loading_animation("generating routing number",2.5);
        return tempRN;
        
    




    def __generateAccountNumber__(self):
        loading_animation("generating account number",2.5);
        tempAC = "";
        for i in range(SIZE_OF_ACCOUNT_NUMBER):
            currentCharacter = random.choice(string.ascii_uppercase + string.digits);
            tempAC += currentCharacter;
    
        if tempAC == "":
            tempAC = DEFAULT_ACCOUNT_TYPE;
            print("--![Account]Operation Failed!--"); 
        self.accountNumber = tempAC;
        return tempAC;
    



    def __updateDict__(self):
        loading_animation("updating internal operations",1.5);
        if self.numberOfAccounts > 1 and self.numberOfAccounts <= MAX_NUMBER_OF_ACCOUNTS:
            # if this is the second account, add a new pair of routing and account numbers
            if len(self.classDict[self.name]) == 2: 
                newRoutingNumber = self.__generateRoutingNumber__();
                newAccountNumber = self.__generateAccountNumber__();
                self.classDict[self.name][0] = [newRoutingNumber, newAccountNumber];
                
                newRoutingNumber = self.__generateRoutingNumber__();
                newAccountNumber = self.__generateAccountNumber__();
                self.classDict[self.name][1] = [newRoutingNumber, newAccountNumber];

            # update the existing pair of routing and account numbers
        else:
            self.routingNumber = self.__generateRoutingNumber__();
            self.accountNumber = self.__generateAccountNumber__();
            self.classDict[self.name][0] = self.routingNumber;
            self.classDict[self.name][1] = self.accountNumber;
            


    
    def __showAccountNumber___(self):
        currentAC = self.__generateAccountNumber__();
        print(f"Your Account Number is: {currentAC}");




    def __showRoutingNumber__(self):
        currentRN = self.__generateRoutingNumber__();
        print(f"Your Routing Number is: {currentRN}");

   


    def __showClassDictionary__(self):
        """
        Function(void): This function calls private method "__updateDict__()" to update the class' dictionary before being used. 
        It loops through the class dictionary with the key and then sets the values as an iterator as well and finally uses the number of accounts to iterate through the values.
        It checks for number accounts and carefully assigns the values to their respective variables
        """
        self.__updateDict__();
        for key in self.classDict:
            values = self.classDict[key]
            print(f"{key}'s Bank Details:")
            for i in range(self.numberOfAccounts):
                if self.numberOfAccounts > 1:
                    routingNumber = values[i][0]
                    accountNumber = values[i][1]
                else:
                    routingNumber = values[i];
                    accountNumber = values[i];
                
                print(f"  Account {i+1}: Routing Number: {routingNumber}, Account Number: {accountNumber}")





    def __selectAccountType__(self):
        """
        Function(void): This Uses the private member"__showClassDictionary__" to prompt the user on what type of account
        Should be assigned. It does so by displaying the current routing and account number and letting the user choose from there. 
        There exists only ttwo types of accounts for this project, "checking" and "savings". s
        """
        self.__showClassDictionary__()
        for key in self.classDict:
            values = self.classDict[key]
            for i in range(self.numberOfAccounts):
                if self.numberOfAccounts > 1:
                    routingNumber = values[i][0]
                    accountNumber = values[i][1]
                else:
                    routingNumber = values[i];
                    accountNumber = values[i+1];
                print(f"Assign account type for account {i+1}:")
                accountType = input("Enter 'C' for Checking or 'S' for Savings: ")
                if accountType.lower() == 'c':
                    self.classDict[key][i] = ['Checking', routingNumber, accountNumber]
                elif accountType.lower() == 's':
                    self.classDict[key][i] = ['Savings', routingNumber, accountNumber]
                else:
                    print("Invalid account type entered. Please enter 'C' for Checking or 'S' for Savings.")
        print("Account types assigned successfully.")
       

 #public member(s):

    def confirm_deposit(self,newAmount,accountType):
        if self.numberOfAccounts ==1:
            self.__deposit__(newAmount);
            pass;
        if self.numberOfAccounts > 1:
            if(accountType == "checking"):
                v = int(newAmount);
                self.checking_balance += v;
                loading_animation("Performing Depost action",2)
                print();
                print(f"${newAmount} has been successfully deposited\nCurrent Checking balance: ${self.checking_balance} ");

                self.classDict[self.name][0][3]= self.checking_balance;



            else:
                v = int(newAmount);
                self.savings_balance += v;
                loading_animation("Performing Depost action",2)
                print();
                print(f"${newAmount} has been successfully deposited\nCurrent Savings balance: ${self.savings_balance} ");
                self.classDict[self.name][1][3]= self.savings_balance;

    

    def confirm_withdrawal(self,amountTaken,accountType):
        if self.numberOfAccounts ==1:
            self.__deposit__(amountTaken);
            pass;
        if self.numberOfAccounts > 1:
            if(accountType == "checking"):
                v = int(amountTaken);
                self.checking_balance -= v;
                loading_animation("Performing Withdrawl action",2)
                print();
                print(f"${amountTaken} has been successfully deducted\nCurrent Savings balance: ${self.savings_balance} ");
                

            else:
                v = int(amountTaken);
                self.savings_balance -= v;
            loading_animation("Performing Withdrawl action",2)
            print();
            print(f"${amountTaken} has been successfully deducted\nCurrent Savings balance: ${self.savings_balance} ");

    



    def displayAccounts(self):
        """
        (Public)(Void) Function: This method makes use of the private method "__selectAccountType__()" to distinguish between accounts using their type. 
        It makes use of an if statement which checks the number of account while looping  through the class' dictionary to display the accounts 
        """
        self.__selectAccountType__();
        for key in self.classDict:
            print(f"{key}'s Bank Details:")
            for i in range(self.numberOfAccounts):
                if self.numberOfAccounts > 1: 
                    account_type = self.classDict[key][i][0]
                    routingNumber = self.classDict[key][i][1]
                    accountNumber = self.classDict[key][i][2]
                else:
                    account_type = self.classDict[key][0][0]
                    routingNumber = self.classDict[key][0][1]
                    accountNumber = self.classDict[key][0][2]
                    
                print(f"  Account {i+1}: Type: {account_type}, Routing Number: {routingNumber}, Account Number: {accountNumber}")




    def distributeBalance(self):
        """
        (Public)(Void) Function: This method prompts the user to distribute the balance initially given from the User class. It does a math check to make sure more than the balance is not being use.
        [Possible Optimization]--> if change remains store it in the user or bank class and print it to the file. 
        """
        for key in self.classDict:
            for i in range(self.numberOfAccounts):
                account_type = self.classDict[key][i][0]
                routingNumber = self.classDict[key][i][1]
                accountNumber = self.classDict[key][i][2]
                balance = self.balance
                if self.numberOfAccounts == 1:
                    self.classDict[key][i].append(balance)
                    print(f"All balance deposited into {account_type} account with Routing Number: {routingNumber} and Account Number: {accountNumber}")
                else:
                    if i == 0:
                     print(f"Enter amount to deposit into {account_type} account with Routing Number: {routingNumber} and Account Number: {accountNumber}\n\tAmount to Deposit: ${balance}")
                    else:
                        print(f"Enter amount to deposit into {account_type} account with Routing Number: {routingNumber} and Account Number: {accountNumber}\n");
                   
                    amount = float(input("$"))
                    if amount > balance:
                        print("Invalid amount entered. Please enter a valid amount.");
                        loading_animation("re-indexing operation[Contact Help center if money was lost in the process.]")
                        self.distributeBalance();
                    else:
                        self.classDict[key][i].append(amount)
                        self.balance -= amount
                        balance = self.balance;
                        print(f"\t${amount} deposited into {account_type} account with Routing Number: {routingNumber} and Account Number: {accountNumber}")
                        print(f"NOTE: You have ${self.balance} left.\n")
                        
        print(f"\nYour change is ${self.balance}\nBalance distributed successfully.")




    def displayAccountBalances(self):
        """
        (Public)(Void) Function: This basically shows the balance each type of account has. 
        Should be called after "distributeBalance()".
        [Possible Optimization]--> display change, as discussed in "distributeBalance()".
        """
        for key in self.classDict:
            checkingBalance = 0
            savingsBalance = 0
            if self.numberOfAccounts > 1:
                for i in range(self.numberOfAccounts):
                    account_type = self.classDict[key][i][0]
                    balance = self.classDict[key][i][3]
                    if account_type == 'Checking':
                        checkingBalance += balance
                    elif account_type == 'Savings':
                        savingsBalance += balance
                print(f"\n{key}'s Account Balances: \n\nChecking Account: ${checkingBalance}\nSavings Account: ${savingsBalance}\nTotal Account Balance: ${checkingBalance+savingsBalance}");
            else:
                checkingBalance+= self.classDict[key][0][3];
                print(f"{key}'s Account Balance: \n{self.classDict[key][0][0]}: ${checkingBalance}\nWith change: ${self.balance}")    



    def saveCustomerInfo(self):
        """
        (Public)(Void) Function: Opens the file {"BankUsersInfo.txt" as 'W+'} and prints the necessary contents of each account. Like name, account type, routing number, account number, and balance.
         [Possible Optimization]--> print with change and today's date. 
        """
        #self.__updateDict__();
        with open("BankUsersInfo.txt","w+") as sourceFile:
             # print the user's name to the file
            sourceFile.write(f"Bank_User_name: {self.name}\n")
            sourceFile.write(f"{self.name}'s age: {self.age}\n")
            sourceFile.write(f"{self.name}'s gender: {self.gender}\n")
            sourceFile.write(f"{self.name}'s number of account(s): {self.numberOfAccounts}\n")

            #,User,routingNumber,accountNumber,checking_balance,savings_balance, checking_routing_number,savings_routing_number, checking_account_number, savings_account_number
            #age,gender,numberOfAccounts,balance = 0.00
            # for each account the user has
            for account, details in self.classDict.items():
                for i in range(len(details)):
                    account_type = details[i][0]
                    routingNumber = details[i][1]
                    accountNumber = details[i][2]
                    balance = details[i][3]

                    sourceFile.write(f"-----------Beginning {account_type} section -------------\n")
                    sourceFile.write(f"{self.name}'s {account_type} Balance: {balance}\n")
                    sourceFile.write(f"{self.name}'s {account_type} Routing Number: {routingNumber}\n")
                    sourceFile.write(f"{self.name}'s {account_type} Account Number: {accountNumber}\n")
                    sourceFile.write(f"-----------Ending {account_type} section -------------\n")

                    if account_type == "checking":
                        balance = self.checking_balance;
                    if account_type == "savings":
                       balance =  self.savings_balance ;
                    
                    if self.balance > 0.00:
                        sourceFile.write(f"You have been refunded  ${self.balance}\n")
                    elif self.balance < 0.00:
                         sourceFile.write(f"You have a deficit of -${abs(self.balance)}\n")
                    else:
                         sourceFile.write(f"You have no change\n")
        loading_animation("Saving Info to the DataBase")
        print("****Successfully printed to file.****")

    
    

    def read_Bank_User_Info(self,filename = "BankUsersInfo.txt"):
        """
        (Void)Function: *help from Chat-Gpt for structure of code*
        """
        with open(filename, 'r') as f: #fix this
            lines = f.readlines()
            name = lines[0].split(': ')[1].strip()
            age = int(lines[1].split(': ')[1]); 
            gender = lines[2].split(': ')[1]; 
            num_of_accts = int(lines[3].split(': ')[1])
            checking_balance = float(lines[11].split(': ')[1])
            checking_routing_number = lines[12].split(': ')[1].strip()
            checking_account_number = lines[13].split(': ')[1].strip()
            savings_balance = float(lines[5].split(': ')[1])
            savings_routing_number = lines[6].split(': ')[1].strip()
            savings_account_number = lines[13].split(': ')[1].strip()
            return name,age,gender,num_of_accts,checking_balance, checking_routing_number, checking_account_number, savings_balance, savings_routing_number, savings_account_number
   
    def login(self):
        """
        (Void)Function: *help from Chat-Gpt for structure of code*
        """
        filename = 'BankUsersInfo.txt'

        name = input("Please enter your name: ")
        password = input("Please enter your password (last 4 digits of your routing number): ")

        try:
            
                user_info = self.read_Bank_User_Info(filename)
                self.name = user_info[0];
                self.age = user_info[1];
                self.gender = user_info[2];
                self.numberOfAccounts = user_info[3];
                self.checking_balance = user_info[4];
                self.savings_balance = user_info[7];
                self.checking_routing_number = user_info[5];
                self.checking_account_number = user_info[6];
                self.savings_account_number = user_info[9];
                self.savings_routing_number = user_info[8];
               
               

                temp_dict = { self.name :{
                        0: ["checking", self.checking_routing_number,self.checking_account_number,self.checking_balance],
                        1: ["savings",self.savings_routing_number,self.savings_account_number,self.savings_balance]
                    }
                }
                self.classDict.update(temp_dict);
                del self.classDict[''];
                
                if name == user_info[0] and (password == self.checking_routing_number[-4:] or password == self.savings_routing_number [-4:]):
                    print("***You're in !***")
                    print(f"Checking balance: ${self.checking_balance:.2f}")
                    print(f"Checking routing number: {self.checking_routing_number}")
                    print(f"Checking account number: {self.checking_account_number}")
                    print(f"Savings balance: ${self.savings_balance:.2f}")
                    print(f"Savings routing number: {self.savings_routing_number}")
                    print(f"Savings account number: {self.savings_account_number}")

                    
                    modifyInfo = input("Do you want to perform any action on your account[yes|no]:");
                    if modifyInfo.lower() == "yes":
                        #could have put in a function but it became super complicated.
                        print("\nChoose an action:")
                        print("1. Deposit money")
                        print("2. Withdraw money")
                        action = input("Enter action number: ")
                        if action == "1" or action == "2":
                            account_name = input("Enter account name: ")
                            if account_name in temp_dict[self.name][0] or  account_name in temp_dict[self.name][1]:
                                if action == "1": #deposit
                                    deposit_amount = float(input("Enter amount to deposit: "));    
                                    self.confirm_deposit(deposit_amount,account_name);
                                    self.saveCustomerInfo();
                                    print("Thank you for Banking with us!")

                                elif action == "2": #withdraw
                                   withdraw_amount = float(input("Enter amount to deposit: "));    
                                   self.confirm_withdrawal(withdraw_amount,account_name);
                                   self.saveCustomerInfo();
                                   print("Thank you for Banking with us!") 
                            else:
                                print("Invalid account name entered")
                        else:
                            print("Invalid action selected")

                    elif modifyInfo.lower() == "no":
                        print("Thank you for Banking with us!")
                        self.saveCustomerInfo();
                        pass;

                else:
                    print("(User Error)Login failed. Please try again.")
          
               
        except FileNotFoundError:
            print(f"(Code Error)File '{filename}' not found.")




def loading_animation(text, duration=6):
    start_time = time.time() # get the start time
    end_time = start_time + duration # calculate the end time
    while time.time() < end_time:
        for i in range(5):
            time.sleep(0.5) # pause for half a second
            loading_message = f"{'.' * i}"
            print(f"{loading_message}\r{text}", end="", flush=True) # print loading message with text below
        print("\r" + " " * 100 + "\r", end="")  # clear the line and overwrite it with 100 whitespaces
    print(f"Done {text}!") # print a message when the animation is finished
   




#Plan: Use a dictionary to determine what current account is being used at the moment for the user.
    # store users information into a file; [--Done]
    # for verification use the User's name and last 4 digits of user's routing number to access account[--Done];
    

def main():
    print("******\tWelcome to EKO Automated Bank System\t*****\n");
    loading_animation("Loading Bank Application");

    continueProgram = int(input("Select an Option:\n1.Existing user?\n2.New User?\n>>"));

    if continueProgram == EXISTING_USER:
        
        knownUser = User(DEFAULT_STRING, DEFAULT_INT, DEFAULT_STRING, DEFAULT_INT, DEFAULT_FLOAT);
        known_Bank_User = Bank(knownUser);
        known_Bank_User.login();
    
        

    elif continueProgram == NEW_USER:

         #STAGE 1
        #let's make it interactive: [to optimize]: verify entries before initializing classes.
        user_John = User(DEFAULT_STRING, DEFAULT_INT, DEFAULT_STRING, DEFAULT_INT, DEFAULT_FLOAT); #Initialising User class  
        user_John.getUserInfo(); #getting user info; 
        loading_animation("--Verifiying info--");

        #STAGE 2
        Chase_John = Bank(user_John); #initialising Bank class
        Chase_John.displayAccounts(); 
        Chase_John.distributeBalance();
        loading_animation("--Calculating Balance--");

        #STAGE 3
        Chase_John.displayAccountBalances();
        Chase_John.saveCustomerInfo();
        loading_animation("Saving Customer Info", 12);
        
    else:
        print("Invalid Choice!\nPlease Try again\n");
        loading_animation("Restarting Program");
        main();



   
    

#calling main.
main();

    

