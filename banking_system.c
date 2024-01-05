/*
1. Create an online banking system with the following features:
* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct user{
    char username[256];
    char password[256];
    float balance;
}user;

int main(){
    //initializing variables
    int log_in_counter = 0;
    int counter;
    int user_counter=0;
    int option;
    int second_option;
    float amount;
    int menu1 = 1;
    int menu2;
    int aux;
    int flag_log_in;
    int flag_transaction;
    user users[256];
    char *ptruser, *ptrpassw;

    while(menu1 == 1){
        printf("Banking System\n1- Create account\n2- Log in\n3- Exit\n");
        scanf("%i",&option);
        switch (option)
        {
        //Creating an account
        case 1:
        //Defining an address in memory for each pointer 
            ptruser = malloc(sizeof(char));
            ptrpassw = malloc(sizeof(char));
            printf("\nEnter a  new username, no blank spaces:");
            scanf("%s",ptruser);
            printf("\nEnter a new password, no blank spaces:");
            scanf("%s",ptrpassw);
            strcpy(users[user_counter].username,ptruser);
            strcpy(users[user_counter].password,ptrpassw);
            users[user_counter].balance = 2000;
            user_counter ++;
            printf("\nNew user %s , new password %s, balance:%f\nAccount created successfully\n\n",users[user_counter-1].username,users[user_counter-1].password,users[user_counter-1].balance);
            free(ptruser);
            free(ptrpassw);
            ptruser = NULL;
            ptrpassw = NULL;
            break;
        //Log in
        case 2:
            if(user_counter==0){
                printf("there no users in the system, please create an user\n");
                break;
            }else{
                ptruser = malloc(sizeof(char));
                ptrpassw = malloc(sizeof(char));
                printf("\nEnter your credentials\nUsername:");
                scanf("%s",ptruser);
                printf("\nEnter yous password\n");
                scanf("%s",ptrpassw);
                counter = 0;
                flag_log_in=0;
                while (counter < user_counter) {
                    if(log_in_counter < 3){
                        if(0 == strcmp(ptruser,users[counter].username) && 0 == strcmp(ptrpassw,users[counter].password)){
                            free(ptruser);
                            ptruser = NULL;
                            flag_log_in=1;
                            menu2=1;
                            printf("\nValid Credentials\n\n");
                            while(menu2 == 1){
                                printf("Select an operation:\n1-Withdraw\n2-Deposit\n3-View balance\n4-Transfer\n5-Exit\n");
                                scanf("%i",&second_option);
                                switch (second_option){
                                    //Withdraw
                                    case 1:
                                        printf("\nHow much do you want to withdraw?:");
                                        scanf("%f",&amount);
                                        if(amount > users[counter].balance || amount <= 0){
                                        printf("Invalid amount, try again\n\n");
                                        }else{
                                            users[counter].balance = users[counter].balance - amount;
                                            printf("Withdraw Successful\n\n");
                                        }
                                        break;
                                    //Desposit
                                    case 2:
                                        printf("\nHow much do you want to deposit?");
                                        scanf("%f",&amount);
                                        if(amount<=0){
                                            printf("Invalid amount, try again\n");
                                        }else{
                                            users[counter].balance = users[counter].balance + amount;
                                            printf("Deposit successful\n\n");
                                        }
                                        break;
                                    //View Balance
                                    case 3:
                                        printf("Your Balance is %f\n\n",users[counter].balance);
                                        break;
                                    //Transfer
                                    case 4:
                                        if(user_counter<2){
                                            printf("Too few users, create more accounts\n\n");
                                            break;
                                        }else{
                                            ptruser = malloc(sizeof(char));
                                            aux = 0;
                                            printf("Transaction Menu\nWrite the user ID to which transfer the money(it's the same as their username)\nUser ID:");
                                            scanf("%s",ptruser);
                                            flag_transaction=0;
                                            while(aux < user_counter){
                                                if(0 == strcmp(ptruser,users[aux].username)){
                                                    flag_transaction=1;
                                                    printf("How much money do you want to transfer?:");
                                                    scanf("%f",&amount);
                                                    if(amount > users[counter].balance || amount <=0){
                                                        printf("Invalid amount\n\n");
                                                        break;
                                                    }else{
                                                        printf("\nSuccessfull transtion\n\n");
                                                        users[aux].balance = users[aux].balance + amount;
                                                        users[counter].balance = users[counter].balance - amount;
                                                    }
                                                }
                                                aux++;                                       
                                            }
                                            if(flag_transaction==0){
                                                printf("\nWrong ID, try again\n\n");
                                            }
                                            free(ptruser);
                                            ptruser = NULL;
                                        }
                                        break;
                                    //Exit
                                    case 5:
                                        menu2=0;
                                        break;
                                    default:
                                        printf("Invalid option, try again\n\n");
                                        break;
                                }
                            }
                            break;
                        }
                    }
                    //Locking out the user 
                    counter++;
                }
                free(ptruser);
                free(ptrpassw);
                ptrpassw= NULL;
                ptruser = NULL;
                if(flag_log_in==0){
                    printf("Wrong Credentials\n\n");
                    log_in_counter++;
                }
                if(log_in_counter==3){
                    printf("Too many attempts, Locking the System\n\n");
                    menu1=0;
                }
                counter = 0;
                break;
            }
        case 3:
            menu1 = 0;
            break;
        default:
            printf("\nInvalid option, try again\n\n");
            break;
        }
    }
    return 0;
}