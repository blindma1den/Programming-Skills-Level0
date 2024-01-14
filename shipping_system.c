/*4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


int main(){
    srand(time(NULL));
    int menu1 = 1;
    int menu2;
    int option1;
    int option2;
    char name_sender[20];
    char name_reciever[20];
    char username[20];
    char password[20];
    char * ptrusername;
    char * ptrpassword;
    float weight;
    float price;
    int log_in_counter = 0;
    //MENU
    while(menu1==1){
        printf("Shipping System\n1-Create an Account\n2-Send a package\n3-Exit\n\n");
            scanf("%i",&option1);
            //Creating an account
            switch(option1){
                case 1:
                    printf("\nEnter a username:");
                    scanf("%s",username);
                    printf("\nEnter a passoword:");
                    scanf("%s",password);
                    printf("Account created successfuly\n");
                break;
                //Log in
                case 2:
                    menu2 = 1;
                    while(menu2==1){
                        ptrusername = malloc(sizeof(char));
                        ptrpassword = malloc(sizeof(char));
                        printf("\nLog In\nEnter your username:");
                        scanf("%s",ptrusername);
                        printf("\nNow enter the password:");
                        scanf("%s",ptrpassword);
                        if(0 == strcmp(ptrusername, username) && 0 == strcmp(ptrpassword,password)){
                            //Details for the sending process
                            printf("\nPlease enter your name:");
                            scanf("%s",name_sender);
                            printf("\nEnter the name of the reciever:");
                            scanf("%s",name_reciever);
                            printf("\nNow specify the weight of the package:");
                            scanf("%f",&weight);
                            price = weight * 2;
                            printf("The price for sending the package would be:%f , and the package number is %i\nThe package will be delivered soon!\n",price,rand());
                            printf("\nYou desire to send another package?\n1-Yes\n2-No\n\n");
                            scanf("%i",&option2);
                            //Send another package or not
                            switch(option2){
                                case 1:
                                    break;
                                case 2:
                                    menu2 = 0;
                                    menu1 = 0;
                                    break;
                                default:
                                    menu2 = 0;
                                    menu1 = 0;
                                    break;
                            }
                        }
                        else{
                            //Wrong log in
                            printf("\nWrong Credentials\n");
                            log_in_counter++;
                            if(log_in_counter == 3){
                                menu2 = 0;
                                menu1 = 0;
                                printf("\nToo many attempts");
                                break;
                            }
                        }
                    }
                    break;
                case 3:
                    menu1 = 0;
                    break;
                default:
                    menu1 = 0;
                    break;
            }
    }
    return 0;
}