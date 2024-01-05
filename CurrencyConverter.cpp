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
    float balanceini =2000;
    int numero;
    int monto=0;
    int x=0;
    int opcion = 0;
    float CLP = 887.89;
	 float ARS = 811.58;
	 float USD = 1 ;
	 float EUR = 0.91;
	 float TRY = 29.75;
	 float GBP =  0.79;
    int   monedae;
    float balanceaux;
    int YN=-1;
    float comision=0;
    int menu3=0;
    int menu=-1;

   while ( strcmp(texto, u1)!=0  && strcmp(password, p1)!=0)

    {

   	 printf("Introduce tu nombre: \n ");
       scanf("%s", texto);

     	 printf("Introduce tu Password: \n ");
   	 scanf("%s", password);

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

		while ( menu != 0 )

   	 {
    	   printf("Hola Bienvenido, %s\n", texto);
      	printf(" \n Menu de Opciones \n");
        	printf("1.Exchange currencies \n");
        	printf("0.Exit \n");
        	printf("Choose Your option: \n");
        	cin>>menu;

        			if ( menu == 1 )
               		{
                					while (monedae!=0)
         								{

         								printf("My current amount convert to: \n");
         								printf("1.CLP \n");
         								printf("2.ARS \n");
         								printf("3.USD \n");
         								printf("4.EUR \n");
         								printf("5.TRY \n");
         								printf("6.GBP \n");
         								printf("0.Exit \n");
         								printf("Choose your currency: \n ");
         								cin>> monedae;

         										if (monedae == 1)
                 									{
                  									balanceaux = balanceini * CLP;
                  									printf ("The change to the new currency is: %f \n ", balanceaux);
                        						}

               								if (monedae == 2)
                									 {
                  									balanceaux = balanceini * ARS;
                  									printf ("The change to the new currency is: %f \n ", balanceaux);
                       							 }

               								if (monedae == 3)
              									   {
                  									balanceaux = balanceini * USD;
                  									printf ("The change to the new currency is: %f \n ", balanceaux);
                        						}

               								if (monedae == 4)
                 									{
                  									balanceaux = balanceini * EUR;
                  									printf ("The change to the new currency is: %f \n ", balanceaux);
                        						}

               								if (monedae == 5)
                									 {
                  									balanceaux = balanceini * TRY;
                  									printf ("The change to the new currency is: %f \n ", balanceaux);
                        						  }

               								if (monedae == 6)
                 									{
                  									balanceaux = balanceini * GBP;
                  									printf ("The change to the new currency is: %f \n ", balanceaux);
                        						}

                										printf("Do you want to change? Y=1 N=0 \n ");
                										cin>>YN;

                 									  	if (YN == 1)
                        								   {
                           									comision = balanceaux * 0.01;
                              							  	balanceaux = balanceaux - comision;
                             								   balanceini = balanceaux;
                                                   }


                                     }
                      }

          }

    }
system("PAUSE");

return 0;
}

