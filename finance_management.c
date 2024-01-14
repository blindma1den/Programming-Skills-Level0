/*
5. Develop a finance management application with the following features:
* 		The user records their total income.
* 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 		The user can list their expenses within the categories and get the total for each category.
* 		The user can obtain the total of their expenses.
* 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
* 		If the user spends more than they earn, the system will display advice to improve the user's financial health.
*/

#include <stdio.h>
#include <stdlib.h>

int main(){
    int menu1 = 1;
    int menu2;
    int option1 ;
    int option2;
    int income=0;
    //0 medicine, 1 houseshold, 2 leisure, 3 savings, 4 educatation
    float expenses[5];
    for(int i = 0; i < 5;i++){
        expenses[i]=0;
    }
    float amount;
    float total_expenses=0;
    int index;

    while(menu1 == 1){
        printf("Finance Maanagement Menu\n1-Record total income\n2-Record expenses\n3-View total expenses\n4-Exit\n\n");
        scanf("%i",&option1);
        //Selecting an action
        switch(option1){
            //Reading the income
            case 1:
                printf("Enter your monthly income:");
                scanf("%i",&income);
                printf("\n");
                break;
            case 2:
            //Reading the expenses
                menu2 = 1;
                while(menu2 == 1){
                    amount = 0;
                    printf("Select a Categorie:\n1-Medical expenses\n2-Household expenses\n3-Leisure\n4-Savings\n5-Education\n6-Exit\n\n");
                    scanf("%i",&option2);
                    switch(option2){
                        case 1:
                            printf("Enter the amount:");
                            scanf("%f",&amount);
                            expenses[0] = expenses[0] + amount;
                            break;
                        case 2:
                            printf("Enter the amount:");
                            scanf("%f",&amount);
                            expenses [1]= expenses[1] + amount;
                            break;
                        case 3:
                            printf("Enter the amount:");
                            scanf("%f",&amount);
                            expenses[2] = expenses[2] + amount;
                            break;
                        case 4:
                            printf("Enter the amount:");
                            scanf("%f",&amount);
                            expenses[3] = expenses[3] + amount;
                            break;
                        case 5:
                            printf("Enter the amount:");
                            scanf("%f",&amount);
                            expenses[4] = expenses[4] + amount;
                            break;
                        case 6:
                            menu2=0;
                            break;
                        default:
                        menu2=0;
                        menu1=0;
                        break;
                    }
                    printf("\n");
                }
            break;
            case 3:
            //See the total expenses and the amount in each category
                printf("These are you expenses by category\nMedicine expenses:%f\n",expenses[0]);
                printf("Household expenses:%f\nLeisure:%f\nSavings:%f\nEducaction:%f\n\n",expenses[1], expenses[2], expenses[3], expenses[4]);
                for(int i = 0; i < 5;i++){
                    total_expenses = total_expenses + expenses[i];
                }
                printf("Your total expenses are:%f\n\n",total_expenses);
                if(total_expenses == income){
                    index = 0;
                    for(int i = 1; i < 4; i++){
                        if(expenses[index]<expenses[i]){
                            index = i ;
                        }
                    }
                    switch(index){
                        case 0:
                        printf("Yo should reduce your expenses in Medicines\n");
                            break;
                        case 1:
                            printf("You should reduce your expenses in Household\n");
                            break;
                        case 2:
                            printf("You should reduce your expenses in Leisure\n");
                            break;
                        case 3:
                            printf("You should reduce your expenses in Savings\n");
                            break;
                        case 4:
                            printf("You should reduce your expeneses in Education\n");
                            break;
                        default:
                        break;
                    }   
                }else{
                    if(total_expenses < income){
                        printf("Congratulations\n\n");
                    }else{
                        printf("You need to improve your financial health\n\n");
                    }
                }
                break;
            case 4:
                menu1=0;
                break;
            default:
                menu1=0;
            break;
        }
    }
    return 0;
}