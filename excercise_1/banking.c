/*
1. Create an online banking system with the following features:
	* Users must be able to log in with a username and password.
	* If the user enters the wrong credentials three times, the system must lock them out.
	* The initial balance in the bank account is $2000.
	* The system must allow users to deposit, withdraw, view, and transfer money.
	* The system must display a menu for users to perform transactions.2.
*/

// Libraries used for this excercise
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <conio.h>

struct user
{
	char username[30];
	char password[30];
	int balance;
	int failedAttempts;
};

// Global Variables
// Convertion based on the usd exchange rate
struct user users[2] = {{"roger", "12345", 2000, 0}, {"maria", "12345", 2000, 0}};
int size = sizeof(users) / sizeof(users[0]);
bool logedIn = false;
int currentUser;
int menuOpt;
char auxUser[30];
char auxPassword[30];
char anyK;

// Function that returns user position in the users array.
int getID(char *usr)
{
	int val = -1;
	for (int i = 0; i < size; i++)
	{
		if (strcmp(users[i].username, usr) == 0)
		{
			val = i;
		};
	};
	return val;
};

// Function that compares if password for the user is correct.
bool login(int id, char *passw)
{
	if (strcmp(users[id].password, passw) == 0)
	{
		return true;
	}
	else
	{
		users[id].failedAttempts++;
		return false;
	}
}

int main()
{
	printf("Welcome to the RBank banking system\n");
	printf("-----------------------------------\n");
	while (1)
	{
		// Login section
		if (!logedIn)
		{
			printf("Please input username: ");
			fflush(stdin);
			scanf("%s", auxUser);
			currentUser = getID(auxUser);
			if (currentUser > -1)
			{
				printf("Please input password: ");
				fflush(stdin);
				scanf("%s", auxPassword);
				if (users[currentUser].failedAttempts < 3)
				{
					bool log = login(currentUser, auxPassword);
					if (log)
					{
						logedIn = true;
						printf("-----------------------------------\n");
						printf("Login Succesfull\n");
						printf("-----------------------------------\n");
					}
					else
					{
						printf("-----------------------------------\n");
						printf("Wrong Password!!!\n");
						printf("-----------------------------------\n");
					}
				}
				else
				{
					printf("-----------------------------------\n");
					printf("User is blocked, please go to your nearest RBank office!\n");
					printf("-----------------------------------\n");
				}
			}
			else
			{
				printf("-----------------------------------\n");
				printf("Error, invalid user!\n");
				printf("-----------------------------------\n");
			};
		}
		else
		{
			// Once loged in you can select an operation in the menu.
			menuOpt = -1;
			printf("-> Input 1 to deposit to your account:\n");
			printf("-> Input 2 to withdraw from your account:\n");
			printf("-> Input 3 to view your current balance:\n");
			printf("-> Input 4 to transfer to Another account:\n");
			printf("-> Input 5 to logout:\n");
			printf("-> Input 6 to exit the banking system:\n");
			printf("Select transaction: ");
			fflush(stdin);
			scanf("%d", &menuOpt);
			switch (menuOpt)
			{
			case 1:
				int deposit;
				printf("-> Please input amount you wish to deposit: ");
				fflush(stdin);
				scanf("%d", &deposit);
				users[currentUser].balance += deposit;
				break;
			case 2:
				int withdraw;
				printf("-> Please input amount you wish to withdraw: ");
				fflush(stdin);
				scanf("%d", &withdraw);
				users[currentUser].balance -= withdraw;
				break;
			case 3:
				printf("-----------------------------------\n");
				printf("-> The current balance of your account is: %d\n", users[currentUser].balance);
				printf("-> Press any key to continue ....\n");
				printf("-----------------------------------\n");
				fflush(stdin);
				getch();
				break;
			case 4:
				int amount;
				char recipient[30];
				int recipientID;
				printf("-----------------------------------\n");
				while (true)
				{
					printf("-> Input the username you wish to transfer to: ");
					fflush(stdin);
					scanf("%s", recipient);
					recipientID = getID(recipient);
					if (recipientID > -1)
					{
						printf("-> Input the amount you wish to transfer: ");
						fflush(stdin);
						scanf("%d", &amount);
						if (users[currentUser].balance >= amount)
						{
							users[currentUser].balance -= amount;
							users[recipientID].balance += amount;
						}
						else
						{
							printf("-----------------------------------\n");
							printf("You dont have enough funds, transference aborted!\n");
							printf("-----------------------------------\n");
						}
						break;
					}
					else
					{
						printf("Recipient for transfer doesnt exist. Do you want to try again Y/N: ");
						char try = ' ';
						fflush(stdin);
						scanf("%c", &try);
						if (try == 'N' || try == 'n')
						{
							break;
						}
					}
				}
				printf("-----------------------------------\n");
				break;
			case 5:
				logedIn = false;
				currentUser = -1;
				printf("-----------------------------------\n");
				printf("Please Login again:\n");
				printf("-----------------------------------\n");
				break;
			case 6:
				printf("-----------------------------------\n");
				printf("Thanks for using the RBank banking system:\n");
				printf("-----------------------------------\n");
				goto exit;
				break;
			}
		}
	}
exit:
	return 0;
}