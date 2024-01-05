#include <stdio>
#include <stdlib.h>
#include <string.h>
#include <iostream>

int main()
{
    char texto[40];
    char password[40];
    char u1 [] ="Horacio";
    char p1 [] ="1234";
    char u2 [] ="Lorena";
    char p2 [] ="4567";
    int balanceini =2000;
    int balanceini2 =2000;
    int numero;
    int monto;
    int x=0;

   while ( strcmp(texto, u1)!=0  && strcmp(password, p1)!=0 &&
           strcmp(texto, u2)!=0  && strcmp(password, p2)!=0 )

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
        printf("Hola Bienvenido, %s\n", texto);
        printf(" \n Menu de Opciones \n");
        printf("1.Depositar \n");
        printf("2.Retirar \n");
        printf("3.Ver \n");
        printf("4.Transferir \n");
        printf("Elija una opcion: ");
        cin>> numero;

         if ( numero == 1 )
                        {
         printf("Cuanto Desea depositar: \n ");
         cin>> monto;
         balanceini = balanceini + monto;
         printf ("Su nuevo balance es: %d \n ", balanceini);
                        }

          if ( numero == 2 )
                        {
           printf("Cuanto Desea retirar: \n ");
           cin>> monto;
               			if (monto > balanceini )
                       	 {
                     		printf("No Hay Saldo Suficiente \n");
                         }

                     	 else
                     	 if  (monto <= balanceini )
                        			{
                       				balanceini =   balanceini - monto;
                       				printf ("Su nuevo balance es: %d \n ", balanceini);
                        			}
                         }

           if ( numero == 3 )
                        {
                  printf("Su Balance actual es: %d \n", balanceini);
                         }

           if ( numero == 4 )
                        {

               printf("Cuanto Desea Transferir: \n ");
         	   cin>> monto;
                       if (monto > balanceini )
                       	 {
                     		printf("No Hay Saldo Suficiente \n");
                         }

                     	 else
                     	 if  (monto <= balanceini )
                        			{
                       				balanceini =   balanceini - monto;
                                 balanceini2 = balanceini2 + monto;

                       				printf ("Su nuevo balance es: %d \n ", balanceini);
                                 printf ("El Monto Transferido es: %d \n ", monto);
                                 printf ("Operacion Completada exitosamente \n ");
                        			}
                        }
        }

 else


 if ( strcmp(texto, u2)==0  && strcmp(password, p2)==0 )
    {
        printf("Hola Bienvenido, %s\n", texto);
        printf(" \n Menu de Opciones \n");
        printf("1.Depositar \n");
        printf("2.Retirar \n");
        printf("3.Ver \n");
        printf("4.Transferir \n");
        printf("Elija una opcion: ");
        cin>> numero;

         if ( numero == 1 )
                        {
         printf("Cuanto Desea depositar: \n ");
         cin>> monto;
         balanceini2 = balanceini2 + monto;
         printf ("Su nuevo balance es: %d \n ", balanceini2);
                        }

          if ( numero == 2 )
                        {
           printf("Cuanto Desea retirar: \n ");
           cin>> monto;
               			if (monto > balanceini2 )
                       	 {
                     		printf("No Hay Saldo Suficiente \n");
                         }

                     	 else
                     	 if  (monto <= balanceini2 )
                        			{
                       				balanceini2 =   balanceini2 - monto;
                       				printf ("Su nuevo balance es: %d \n ", balanceini2);
                        			}
                         }

           if ( numero == 3 )
                        {
                  printf("Su Balance actual es: %d \n", balanceini2);
                         }

           if ( numero == 4 )
                        {

         printf("Cuanto Desea Transferir: \n ");
         	   cin>> monto;
                       if (monto > balanceini2 )
                       	 {
                     		printf("No Hay Saldo Suficiente \n");
                         }

                     	 else
                     	 if  (monto <= balanceini2 )
                        			{
                                 balanceini2 = balanceini2 - monto;
                       				balanceini =   balanceini + monto;
                                 printf ("Su nuevo balance es: %d \n ", balanceini2);
                                 printf ("El Monto Transferido es: %d \n ", monto);
                                 printf ("Operacion Completada exitosamente \n ");
                        			}

                         }

    }

 system("PAUSE");

return 0;

}

