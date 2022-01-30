
"""
Created on Sat Jan 29 19:27:06 2022

@author: Ekarsi
"""

import pickle
import os
import pathlib
import random

#account identifiers.
class Account:
    accNo = 0
    name = ''
    deposit=0
    type = ''
    
    def createAccount(self):
        #generating the 12-digit account number.
        self.accNo = int("%0.12d" % random.randint(0,999999999999))
        
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [C/S] : ")
        self.deposit = int(input("Enter The Initial amount (Minimun 500 for Saving and Minimum 1000 for current) : "))
        print("\nAccount Created\n\n")
        
        print("Account Details : \n")
        
        #for giving the details of the new account.
        print("Account No. : ", self.accNo," ","Account Holder Name : ", self.name, " ", 
              "Account Type : ", self.type, " ", "Account Balance : ", self.deposit)
        
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        self.deposit = int(input("Modify Balance :"))
        
    def depositAmount(self,amount):
        self.deposit += amount
    
    def withdrawAmount(self,amount):
        self.deposit -= amount
    
    def report(self):
        print(self.accNo, " ",self.name ," ",self.type," ", self.deposit)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    

def writeAccount():
    '''
    This function creates a new account.

    Returns
    -------
    None.

    '''
    
    account = Account()
    account.createAccount()
    
    #to create the new database.
    writeAccountsFile(account)
    
    

def displayAll():
    '''
    This function display's complete bank database.'

    Returns
    -------
    None.

    '''
    
    #to access the database.
    file = pathlib.Path("accounts.data")
    
    if file.exists ():
        infile = open('accounts.data','rb')
        
        #getting the database as a list.
        details = pickle.load(infile)
        
        #Splitting infos for respective accounts.
        for item in details :
            
            #printing the account details.
            print("Account No. : ", item.accNo," ","Account Holder Name : ", item.name, " ", 
                  "Account Type : ", item.type, " ", "Account Balance : ", item.deposit)
            
        infile.close()
                
    else:
        print("\n\tNo records to display")
        
        

def balanceenquiry(num): 
    '''
    This function provides the info about present account balance. 

    Parameters
    ----------
    num : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    #to access the bank database.
    file = pathlib.Path("accounts.data")
    
    #to check if there is records.
    if file.exists ():
        infile = open('accounts.data','rb')
        
        #getting the database as a list
        details = pickle.load(infile)
        infile.close()
        
        #setting a search flag & defining it.
        found = False
        
        #iteraing over the list.
        for item in details:
            
            #to check if the account exists.
            if item.accNo == num:
                print("Your account Balance is = ",item.deposit)
                
                #redefining the flag.
                found = True
    else:
        print("No records to Search")
        
    if not found:
        print("No existing record with this number")

def depositAndWithdraw(num1,num2): 
    '''
    This function is for deposits & withdrawals.

    Parameters
    ----------
    num1 : TYPE
        DESCRIPTION.
    num2 : TYPE
        DESCRIPTION: Value of 0 indicates deposit & value of 1 indicates withdrawal.

    Returns
    -------
    None.

    '''
    
    #to access the bank database.
    file = pathlib.Path("accounts.data")
    
    #to check if there is records.
    if file.exists ():
        infile = open('accounts.data','rb')
        
        #getting the database as a list
        old_data = pickle.load(infile)
        infile.close()
        
        #deleting the old records file.
        os.remove('accounts.data')
        
        #to iterate over the old data list.
        for item in old_data:
            
            #finding the required account.
            if item.accNo == num1:
                
                #displaying the available balance
                print("\n\tAvailable Balance : ", item.deposit)
                
                #selection for deposit or withdrawal.
                if num2 == 0:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    
                    #displaying the final balance.
                    print("\n\tBalance At Closure : ", item.deposit)
                    print("\n\tYour account is updated")
                    
                #selection for deposit or withdrawal.    
                elif num2 == 1 :
                    amount = int(input("Enter the amount to withdraw : "))
                    
                    #confirming the minimun account balance condition for Savings & Current Account.
                    if item.type == "S" or item.type == "s":
                    
                        #checking if the account have the required balance for withdrawal.
                        if (item.deposit - amount) >= 500:
                            item.deposit -=amount
                            
                            #displaying the final balance.
                            print("\n\tBalance At Closure : ", item.deposit)
                            print("\n\tYour account is updated")
                            
                        else :
                            print("YOU DON'T HAVE ENOUGH BALANCE.")
                    
                    #confirming the minimun account balance condition for Savings & Current Account.
                    elif item.type == "C" or item.type == "c":
                        
                        #checking if the account have the required balance for withdrawal.
                        if (item.deposit - amount) >= 1000:
                            item.deposit -=amount
                            
                            #displaying the final balance.
                            print("\n\tBalance At Closure : ", item.deposit)
                            print("\n\tYour account is updated")
                            
                        else :
                            print("YOU DON'T HAVE ENOUGH BALANCE.")
                
    else:
        print("No records to Search")
        
    #creating a new record file and modifying it with current records.    
    outfile = open('newaccounts.data','wb')
    pickle.dump(old_data, outfile)
    outfile.close()
    
    #renaming the new record file as the old one.
    os.rename('newaccounts.data', 'accounts.data')


    
def deleteAccount(num):
    '''
    This function deletes an account from the bank database.

    Parameters
    ----------
    num : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    #to access the bank database.
    file = pathlib.Path("accounts.data")
    
    #if records are present.
    if file.exists ():
        infile = open('accounts.data','rb')
        
        #creating a list out of the details.
        oldlist = pickle.load(infile)
        infile.close()
        
        #deleting the old records file.        
        os.remove('accounts.data')
        
        #creating an empty new list to store the data after deletion.
        newlist = []
        
        #to iterate over the old data list.
        for item in oldlist:
            
            #to create a new list with the account details that are not to be deleted.
            if item.accNo != num:
                newlist.append(item)
        
             
        #creating a new record file and modifying it with current records.
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        
        #renaming the new record file as the old one.
        os.rename('newaccounts.data', 'accounts.data')
        
        
     
def modifyAccount(num):
    '''
    This function modifies the data for a particular account.

    Parameters
    ----------
    num : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    #to access the bank database.
    file = pathlib.Path("accounts.data")
    
    #if records are present.
    if file.exists ():
        infile = open('accounts.data','rb')
        
        #creating a list out of the details.
        oldlist = pickle.load(infile)
        infile.close()
        
        #deleting the old records file.
        os.remove('accounts.data')
        
        #to iterate over the old data list.
        for item in oldlist:
            
            #finding the required account.
            if item.accNo == num:
                
                #showing the current details present in the records.
                print("\n")
                print("Account No. : ", item.accNo," ","Account Holder Name : ", item.name, " ", 
                      "Account Type : ", item.type, " ", "Account Balance : ", item.deposit)
                print("\n")
                
                #Menu for modification.
                print("\tSELECT WHAT TO MODIFY")
                print("\t1. NAME")
                print("\t2. ACCOUNT TYPE")   
                print("\t3. CURRENT BALANCE")
                print("\t4. ALL DETAILS")
                
                #taking the choice
                choice = input("\tEnter your selection : ")
                
                #selection w.r.t choice.
                if choice == '1':
                    item.name = input("Enter the account holder name : ")
                    print("\nAccount No. : ", item.accNo," ",
                          "Modified Account Holder Name : ", item.name)
                    print("\nName Modified Successfully.")
                    
                elif choice == '2':
                    item.type = input("Enter the account Type : ")
                    print("\nAccount No. : ", item.accNo," ",
                          "Modified Account Type : ", item.type)
                    print("\nAccount Type Modified Successfully.")
                    
                elif choice == '3':
                    item.deposit = int(input("Enter the Amount : "))
                    print("\nAccount No. : ", item.accNo," ",
                          "Modified Account Balance : ", item.deposit)
                    print("\nCurrent Balance Modified Successfully.")
                    
                elif choice == '4':
                    item.name = input("Enter the account holder name : ")
                    item.type = input("Enter the account Type : ")
                    item.deposit = int(input("Enter the Amount : "))
                    print("\nAccount No. : ", item.accNo," ","Modified Account Holder Name : ", item.name, " ", 
                          "Modified Account Type : ", item.type, " ", "Modified Account Balance : ", item.deposit)
                    print("\n Name, Account Type, Current Balance Modified Successfully.")
                    
                else:
                    print("\tInvalid Selection.")
                    return
        
        #creating a new record file and modifying it with current records.
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        
        #renaming the new record file as the old one.
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account):
    '''
    This function creates the record for new account.

    Parameters
    ----------
    account : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    file = pathlib.Path("accounts.data")
    
    #checking if the file already exists.
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        
        #adding the new account in database.
        oldlist.append(account)
        infile.close()
        
        #clearing the previous database.
        os.remove('accounts.data')
        
    else :
        oldlist = [account]
        
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    
    #renaming the new database to previous one.
    os.rename('newaccounts.data', 'accounts.data')
    
        

def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''
    
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")

    print("\t\t\t\t  Brought To You By:")
    print("\t\t\t\t     Ekarsi Lodh")
    
    #defining option
    option = ''
    
    while option != 8:
        
        #Main Menu
        print("\n\n\t  MAIN MENU")
        print("\t1. NEW ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. BALANCE ENQUIRY")
        print("\t5. MODIFY AN ACCOUNT")
        print("\t6. CLOSE AN ACCOUNT")
        print("\t7. ALL ACCOUNT HOLDER LIST")
        print("\t8. EXIT")
        print("\tSelect Your Option (1-8) ")
    
        #taking user choice
        option = input("\tEnter your choice : ")
    
        if option == '1':
            writeAccount()
        
        elif option =='2':
            num = int(input("\tEnter The account No. : "))
            depositAndWithdraw(num, 0)
        
        elif option == '3':
            num = int(input("\tEnter The account No. : "))
            depositAndWithdraw(num, 1)
        
        elif option == '4':
            num = int(input("\tEnter The account No. : "))
            balanceenquiry(num)
        
        elif option == '5':
            num = int(input("\tEnter The account No. to be modified : "))
            modifyAccount(num)
        
        elif option == '6':
            num =int(input("\tEnter The account No. to be closed : "))
            deleteAccount(num)
        
        elif option == '7':
            displayAll()
        
        elif option == '8':
            print("\tThanks for using bank managemnt system")
            break;
    
        else :
            print("The option is not valid. Please re-enter the option.\n")
        
#This will automatically run the main function of ther program.

if __name__ == '__main__':
    main()
    
