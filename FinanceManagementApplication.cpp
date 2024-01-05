#include <stdio>
#include <stdlib.h>
#include <string.h>
#include <iostream>

//Important note.. this program is still under construction..


int main()
{
    char texto[40];
    char password[40];
    char u1 [] ="Horacio";
    char p1 [] ="1234";
    int balanceini =0;
    int numero=-1;
    int monto;
    int x=0;
    float generalexp;
 	 float categoryexp;

   while ( strcmp(texto, u1)!=0  && strcmp(password, p1)!=0 )

    {

    printf("Introduce tu nombre: \n ");
    scanf("%s", texto);

    printf("Introduce tu Password: \n ");
    scanf("%s", password);
    system("cls");
    x= x + 1;

    if (x>=3)
           {
            printf("Ha completado el numero total de intentos \n");
            system("PAUSE");
            exit(-1);
           }
     }


    if ( strcmp(texto, u1)==0  && strcmp(password, p1)==0 )
    {

     while (numero !=0)

     			{

        printf("Hello! Welcome , %s\n", texto);
        printf(" \n CATEGORIES \n");
        printf("1.Medical Expenses \n");
        printf("2.Household Expenses \n");
        printf("3.Leisure \n");
        printf("4.Savings \n");
        printf("5.Education \n");
        printf("0.Exit \n");
        printf("Choose an Option: \n ");
        cin>> numero;

         if ( numero == 1 )
                        {
         printf("Expense entry: \n ");
         cin>> monto;
         categoryexp = categoryexp + monto;
         printf("Do you want to enter another expense Y = 1 N = 0 \n");
         cin>> numero;
         system("cls");
                        }

          if ( numero == 2 )
                        {

         printf("Expense entry: \n ");
         cin>> monto;
         categoryexp = categoryexp + monto;
         printf("Do you want to enter another expense Y = 1 N = 0 \n");
         cin>> numero;


                         }

           if ( numero == 3 )
                        {
         printf("Expense entry: \n ");
         cin>> monto;
         categoryexp = categoryexp + monto;
         printf("Do you want to enter another expense Y = 1 N = 0 \n");
         cin>> numero;
                         }

           if ( numero == 4 )
                        {
         printf("Expense entry: \n ");
         cin>> monto;
         categoryexp = categoryexp + monto;
         printf("Do you want to enter another expense Y = 1 N = 0 \n");
         cin>> numero;
                        }

         	if ( numero == 5 )

                        {
         printf("Expense entry: \n ");
         cin>> monto;
         categoryexp = categoryexp + monto;
         printf("Do you want to enter another expense Y = 1 N = 0 \n");
         cin>> numero;
                        }


        }

     }

 system("PAUSE");

return 0;

}
