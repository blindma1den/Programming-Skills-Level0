user = 'Tomas'
password = '12345678'
valid = False
count = 0

print('Log In')

while valid != True:
    confirmUser = input('User: ')
    
    if(confirmUser == user):
        
        print('Correct User')
        
        while valid != True:
            if(count <= 3): 
                confirmPassword = input('Password: ')
                
                if(confirmPassword == password):
                    print(f'Welcome {user}')
                    valid = True
                else:
                    print('Incorrect Password.')
                    count += 1
            else:
                print('User bloqued due to three incorrect Password attempts.')
                break
    else:
        print('User not found.')

money = 2000

def deposit(m):
    dep = int(input('Deposit Money: '))
    total = m + dep
    
    return total

def whitdraw(m):
    ret = int(input('Whitdraw money: '))
    total = m - ret
    if(total >= 0):
        print('¡Succeful whitdraw!')
    else:
        print('Money not available')
        total = 0
 
    return total

def transfer(m):
    destiny = input('Ingresa CBU, CVU o alias: ')
    
    cant = int(input('Ingresa el monto: '))
    
    confirm = input('Transfer Yes / Not: ').capitalize()
    
    if(confirm == 'Yes'):
        print(f'Transfer in process to {destiny}')

        if(m - cant >= 0):
            total = m - cant
            print('¡Succeful transfer!')
        else:
            print('Money not available. Transfer canceled')
            total = m

    elif(confirm == 'Not'):
        print('transfer canceled')
        total = m
    else:
        print('Incorrect option')
        total = m

    return total 

menu = '''
1_ Deposit.
2_ Whitdraw.
3_View.
4_Transfer Money.
5_Exit.
'''
print(menu)

option = int(input('Elegí una opción: '))

while option != 5:
    if(option == 1):
        print('Option 1')
        funDep = deposit(money)
        money = funDep
        print('¡Succeful deposit!')
        print(f'Money available: ${money}')

    elif(option == 2):
        print('Option 2')
        funRet = whitdraw(money)
        money = funRet
        print(f'Money available: ${money}')
    
    elif(option == 3):
        print('Option 3')
        print(f'You money available: ${money}')
        
    elif(option == 4):
        print('Option 4')
        funTrans = transfer(money)
        money = funTrans
        print(f'Money available: ${money}')
        
    else:
        print('Incorrect option. Repeat')
        
    print(menu)
    
    option = int(input('Elegí una opción: '))
        
print('Exit sistem. Thank you for using my sistem')