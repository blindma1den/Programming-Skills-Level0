/*
3. Create an university enrollment system with the following characteristics:
* 		The system has a login with a username and password.
* 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* 		The user must input their first name, last name, and chosen program.
* 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If login information is incorrect three times, the system should be locked.
* 		The user must choose a campus from three cities: London, Manchester, Liverpool.
* 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
*/
/*
- login with user and password that locks if wrong 3 times
- after login display the programs available
- ask for data and chose program
- max per program 5 changing with locations, programs contain the locations direction and the values for it.
-save users data and show if the limit is exceeded
- the user mush choose a campus
- if program is not available at that campus show the others

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
	int failedAttempts;
	char firstName[30];
	char lastName[30];
};

struct location
{
	char location[30];
	int maxSlots;
	int currentSlots;
};

struct program
{
	char programName[30];
	int maxEnroll;
	int currentEnroll;
	struct location locations[3];
	int users_id[5];
};

// Global Variables
// Convertion based on the usd exchange rate
struct user users[2] = {{"roger", "12345", 0}, {"maria", "12345", 0}};
int size = sizeof(users) / sizeof(users[0]);
// Computer Science, Medicine, Marketing, and Arts
struct program programs[4] = {
	{"Computer Science", 5, 0, {{"London", 1, 0}, {"Manchester", 3, 0}, {"Liverpool", 1, 0}}},
	{"Medicine", 5, 0, {{"London", 1, 0}, {"Manchester", 3, 0}, {"Liverpool", 1, 0}}},
	{"Marketing", 5, 0, {{"London", 1, 0}, {"Manchester", 3, 0}, {"Liverpool", 1, 0}}},
	{"Arts", 5, 0, {{"London", 1, 0}, {"Manchester", 3, 0}, {"Liverpool", 1, 0}}}};

bool logedIn = false;
int currentUser;
int menuOpt;
char auxUser[30];
char auxPassword[30];
char firstName[30];
char lastName[30];
char program[30];
char campus[30];
char catCampus[99];
int selectedProgram;
int selectedCampus;
char auxLocation[30];
char auxProgram[30];

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
	printf("University enrollment system\n");
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
					printf("Too many incorrect attempts at login, user locked\n");
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
			printf("Available programs: Computer Science, Medicine, Marketing and Arts\n");
			printf("Please input your first name: ");
			fflush(stdin);
			gets(users[currentUser].firstName);
			printf("Please input your last name: ");
			fflush(stdin);
			gets(users[currentUser].lastName);
			printf("Please input your chosen program: ");
			fflush(stdin);
			gets(auxProgram);
			// Get the value for the position of the array with all the programs
			if (strcmp(auxProgram, "Computer Science") == 0)
			{
				selectedProgram = 0;
			}
			else
			{
				if (strcmp(auxProgram, "Medicine") == 0)
				{
					selectedProgram = 1;
				}
				else
				{
					if (strcmp(auxProgram, "Marketing") == 0)
					{
						selectedProgram = 2;
					}
					else
					{
						if (strcmp(auxProgram, "Arts") == 0)
						{
							selectedProgram = 3;
						}
					}
				}
			}

			if (programs[selectedProgram].currentEnroll < 5)
			{
				printf("Please select a campus for the program (London, Manchester, Liverpool): ");
				fflush(stdin);
				gets(campus);

				if (strcmp(campus, "London") == 0)
				{
					selectedCampus = 0;
				}
				else
				{
					if (strcmp(campus, "Manchester") == 0)
					{
						selectedCampus = 1;
					}
					else
					{
						if (strcmp(campus, "Liverpool") == 0)
						{
							selectedCampus = 2;
						}
					}
				}
				if (programs[selectedProgram].locations[selectedCampus].currentSlots < programs[selectedProgram].locations[selectedCampus].maxSlots)
				{
					printf("Succesful register in the program.\n");
					// Record Data
					programs[selectedProgram].users_id[currentUser] = currentUser;
					programs[selectedProgram].currentEnroll++;
					programs[selectedProgram].locations[selectedCampus].currentSlots++;
				}
				else
				{
					printf("No more room in this campus for your selected program.\n");
					strcat(catCampus, "( ");
					for (int i = 0; i < 3; i++)
					{
						if (i != selectedCampus && (programs[selectedProgram].locations[i].currentSlots < programs[selectedProgram].locations[i].maxSlots))
						{
							strcat(catCampus, programs[selectedProgram].locations[i].location);
							if ((i + 1) < 3)
							{
								strcat(catCampus, ", ");
							}
						}
					}
					strcat(catCampus, " )");
					printf("Locations with room for your selected program: %s\n", catCampus);
					printf("Please select one of these available locations to finish your register: ");
					fflush(stdin);
					gets(campus);
					if (strcmp(campus, "London") == 0)
					{
						selectedCampus = 0;
					}
					else
					{
						if (strcmp(campus, "Manchester") == 0)
						{
							selectedCampus = 1;
						}
						else
						{
							if (strcmp(campus, "Liverpool") == 0)
							{
								selectedCampus = 2;
							}
						}
					}
					// Record Data
					programs[selectedProgram].users_id[currentUser] = currentUser;
					programs[selectedProgram].currentEnroll++;
					programs[selectedProgram].locations[selectedCampus].currentSlots++;
				}
			}
			else
			{
				printf("This program is unavailable\n");
			}
			menuOpt = -1;
			printf("-> Input 1 to login again:\n");
			printf("-> Input 2 to exit:\n");
			printf("Select operation: ");
			fflush(stdin);
			scanf("%d", &menuOpt);
			switch (menuOpt)
			{
			case 1:
				printf("-----------------------------------\n");
				logedIn = false;
				break;
			case 2:
				goto exit;
				break;
			}
		}
	}
exit:
	return 0;
}