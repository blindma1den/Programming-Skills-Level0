"""
Banking System

"""
import sys
import decimal
import getpass
#Global Vars
MoneyAccount = float(2000)
MoneyTransactions = []
MoneyWithdraws = []
MoneyTransfers = []

def isvalidData(user):
    """Function To Valid username"""
    if user.lower() == "metroid":
        return True
    else:
        return False

def isvalidPasswordStr(password):
    """function to vlaida password"""
    if password.lower() == "batman":
        return True
    else:
        return False
    

def introduction_banking():
    """Function Put Credentials"""
    try:

        print('=============================')
        print('= Banking System =')
        print('=============================')
        choice = 1
        _intento_acceso = 1

        while choice:

            print('=============================')
            getUser = input("Username: ").strip()
            print('=============================')
            getPassword = getpass.getpass('Password:').strip()
            print('=============================')
            strValidUser = isvalidData(getUser)
            strValidPass = isvalidPasswordStr(getPassword)
            #print(f"Usuario Valido: {strValidUser}")
            #print(f"Password Valido: {strValidPass}")
            if bool(strValidUser) and bool(strValidPass):
                print("Datos de Acceso correcto")
                main_system()
            else:
                print(f"Incorrect Data, Please intent again. Wrong #{_intento_acceso}")

                if _intento_acceso >= 3:
                    print("Maximum failed attempts try again.")
                    exit_program()

                _intento_acceso += 1


    except ImportError:
        print("Error de  ejecución")
        exit_program()

def showMenu() -> str:
    """Function to show menu"""
    str_menu = """
    === System Banking Menu ===
        > (1) View Account
        > (2) Deposit Money
        > (3) Withdraw Money
        > (4) Transfer Money
        > (5) Exit
    """
    return str_menu


def main_system():
    """System Principals functions Menu"""
    try:
        _answer=True
        while _answer:
            print(showMenu())
            try:
                _choose = float(input("What would you like to do? "))
            except ValueError:
                print("this is not a valid Option, Try again")
                main_system()

            if _choose:
                """This is valid choose?"""
                while _choose != 0:
                    if _choose == 1:
                        view_account()
                    elif _choose == 2:
                        deposit_amount()
                    elif _choose == 3:
                        withdraw_amount()
                    elif _choose == 4:
                        transfer_amount()
                    elif _choose == 5:
                        exit_program()
                    else:
                        _exitraw = input("Are you sure you want to exit? Y/N:")
                        print(_exitraw)
                        if _exitraw.lower() == 'y':
                            _answer = False
                            exit_program()
                        else:
                            main_system()
            else:
                print("this is not a valid Option, Try again")
                main_system()
    except ImportError :
            print("this is not a valid Option, Try again")
            main_system()

def isValidoption(valueChoosen)->bool:
    """Function to Validate if is Integer option"""
    isvalid = False
    if type(valueChoosen) == int:
        isvalid = True
    else:
        isvalid = False

    return isvalid

def view_account():
    """Function to View Your Account"""
    #print(MoneyTransactions)
    #print(MoneyWithdraws)
    chkhistorytransactions  = chkamount()
    print(f"Your Balance Amount: {format(chkhistorytransactions)}")
    main_system()
def exit_program():
    """Function to Exit program"""
    print("System is turning off.")
    sys.exit(0)

def deposit_amount():
    """Function to Deposit Amount"""
    lop = True

    while lop:
        print("""
            == How many ($) Do Yo Have to Deposit? ==\n 
            """)
        amount = float(input("Amount to Deposit:"))
        #print(f"Amount to Deposit: {amount}")

        if amount == 0:
            print("The Deposit needs to be different that 0, try again")
        else:
            print(f'Waiting, your Amount is adding...')
            for i in range(5):
                if i == 4:
                    MoneyTransactions.append(amount)
            print(MoneyTransactions)
        break
    main_system()


def withdraw_amount():
    """Function to Withdraw Amount"""
    draw_menu = True
    try:
        while draw_menu:
            print("Options to Withdraws: [] 100 [] 200 [] 500 \n")
            print("""
                == Select how much you want to withdraw? == \n""")
            money_withdraw = float(input("Amount to Deposit:"))
            if money_withdraw == 0:
                print(f"your withdrawal need to be different thant: {money_withdraw}, please enter another amount.")
            else:
                amount_totally = chkamount()
                #print(f'Your Amount to withdraw=> {amount_totally}')
                if amount_totally > 0:
                    print(f'Waiting, your Withdraw is executing...')
                    MoneyWithdraws.append(money_withdraw)
                    break
                else:
                    print("You dont have enough money to withdraw")
                    break
        
        main_system()

    except ImportError :
        print("this is not a valid Option, Try again")


def transfer_amount():
    """Function to Do transfer Amount"""
    amount_transfer = chkamount()
    print('='*10)
    print(f"=> Amount Available To Transfer: {amount_transfer}")
    print('='*10)
    _transfer = True
    _digitslenAccount = 16
    while _transfer:
        try:
            transfer_amount = float(input("amount:"))
            if transfer_amount  > chkamount():
                print("You Couldn't transfer that amount, try again")
            else:
                input_account = input("Please enter 16 Digits from Account Number:").replace(" ", "")

            if len(input_account) < _digitslenAccount or len(input_account) > _digitslenAccount:
                print("Your account is incorrect, please type 16 digits to Proceed")
            else:
                print("Transfering Amount")
                MoneyTransfers.append(transfer_amount)
                break
        except Exception as e:
            print(f'Error {e}')
            pass
        finally:
            pass
    main_system()

def chkamount()->float:
    amount = 0.00
    moneybalancepositive = 0
    moneybalancenegative = 0
    moneybalancetransfer = 0
    
    for moneyPositive in MoneyTransactions:
        moneybalancepositive = moneybalancepositive + moneyPositive

    for moneyNegative in MoneyWithdraws:
        moneybalancenegative = moneybalancenegative + moneyNegative

    for moneyTransfered in MoneyTransfers:
        moneybalancetransfer = moneybalancetransfer +  moneyTransfered

    totallyamount = (moneybalancepositive + MoneyAccount) - moneybalancenegative - moneybalancetransfer
    if totallyamount < 0:
        amount = -1.0
    else:
        amount = totallyamount

    return amount

introduction_banking()
