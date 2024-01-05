/* Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.
*/

#include <stdio.h>
//Function for the equivalence between currencies 
float equivalence(int c1, int c2,float amount,float * values){
    float resp;
    float aux;
    if(c2 == 2){
        resp = amount * values[c1];
    }else{
        aux = amount * values[c1];
        resp = aux / values[c2];
    }
    return resp;
}

int main(){
    int menu = 1;
    int option;
    int act_curr;
    float act_amount;
    int fut_curr;
    float fut_amount;
    float comission;
    float curr_values[] = {0.0011 , 0.0012 , 1 , 1.09 , 0.034 , 1.27};
    char *currencies [] = {"CLP","ARS","USD","EUR","TRY","GBP"};
    int valid_amount;

    //Main menu
    while (menu == 1){
        valid_amount = 0;
        printf("Currencies Convertes\nSelect your actual currency\n");
        printf("1-CLP\n2-ARS\n3-USD\n4-EUR\n5-TRY\n6-GBP\n7-Exit\n\n");
        scanf("%i",&act_curr);
        //Exit option
        if(act_curr==7){
            break;
        }else{
            //Selecting a currency
            if(act_curr >= 1 && act_curr <7){
                printf("\nNow write the amount\n");
                scanf("%f",&act_amount);
                //Checking the minimum
                if(act_amount>4.50){
                    //Checking the maximum
                    switch (act_curr){
                        //CLP Maximum
                        case 1:
                            if(act_amount < 1000000){
                                valid_amount=1;
                            }else{
                                printf("The maximum amount for %s is 1000000, try again\n\n",currencies[0]);
                            }
                            break;
                        //ARS Maximum
                        case 2:
                            if(act_amount < 120000.50){
                                valid_amount = 1;
                            }else{
                                printf("The maximum amount for %s is 120000.500 , try again\n\n",currencies[1]);
                            }
                            break;
                        //USD Maximum
                        case 3:
                            if(act_amount <1300.50){
                                valid_amount = 1;
                            }else{
                                printf("The maxium amount for %s is 1300.50 , try again\n\n",currencies[2]);
                            }
                            break;
                        //EUR Maximum
                        case 4:
                            if (act_amount < 1200){
                                valid_amount = 1;
                            }else{
                                printf("The maximum amount for %s is 1200, try again\n\n", currencies[3]);
                            }
                            break;
                        //TRY Maximum
                        case 5:
                            if(act_amount <160000){
                                valid_amount = 1;
                            }else{
                                printf("The maximu amount for %s is 160000, try again\n\n", currencies[4]);
                            }
                            break;
                        //GBP Maximum
                        case 6:
                            if(act_amount < 77777){
                                valid_amount = 1;
                            }else{
                                printf("The maximun amount for %s is 16000, try again\n\n", currencies[5]);
                            }
                            break;
                    }
                    if(valid_amount==1){
                        //Currency to exchange to
                        printf("\nTo continue please select the currency you want to exchange to\n");
                        printf("1-CLP\n2-ARS\n3-USD\n4-EUR\n5-TRY\n6-GBP\n\n");
                        scanf("%i",&fut_curr);
                        //Doing the convertion
                        fut_amount = equivalence(act_curr -1,fut_curr -1 ,act_amount,curr_values);
                        printf("\nYour amount would be %f in the currency %s\n",fut_amount,currencies[fut_curr-1]);
                        //Withdraw or not Withdraw
                        comission = fut_amount * 0.01;
                        printf("Would you like to withdraw ?\n1-Yes (The comission would be %f)\n2-No\n",comission);
                        scanf("%i",&option);
                        if(option == 1){
                            //Another operation or exit
                            printf("Withdraw successful, you amount is:%f\n",fut_amount-comission);
                            printf("You do want to make another operation?\n1-Yes\n2-No\n");
                            scanf("%i",&option);
                            if(option == 1){
                                printf("\n");
                            }else{
                                if(option == 2){
                                    menu = 0;
                                }else{
                                    printf("Invalid option");
                                    menu = 0;
                                 }
                            }
                        }else{
                            printf("\n");
                        }
                    }
                }
                else{
                    printf("The minimun amount for any currency is 4.50 , try again\n\n");
                }
            }else{
                printf("Invalid option");
                menu=0;
            }
        }
    }
    return 0;
}