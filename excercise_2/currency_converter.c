/*
2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
* 		The user must choose their initial currency and the currency they want to exchange to.
* 		The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* 		If the user decides to withdraw the funds, the system will charge a 1% commission.
* 		Set a minimum and maximum amount for each currency, it can be of your choice.
* 		The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process;
otherwise, the system should close.
*/

// Libraries used for this excercise
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <conio.h>

struct rates
{
	float clp;
	float clpMin;
	float clpMax;
	float ars;
	float arsMin;
	float arsMax;
	float usd;
	float usdMin;
	float usdMax;
	float eur;
	float eurMin;
	float eurMax;
	float try;
	float tryMin;
	float tryMax;
	float gbp;
	float gbpMin;
	float gbpMax;
};

// Global Variables
// Convertion based on the usd exchange rate
struct rates exchangeRates = {0.0010471419, 1000.0, 2000000.0, 0.001166118, 100.0, 10000000.0, 1.0, 10.0, 1000000000.0, 1.0834543, 100.0, 1000000.0, 0.031302262, 1000000.0, 10000000.0, 1.2650254, 100000.0, 1000000.0};
bool fundsLoaded = false;
bool firstEntry = true;
int menuOpt;

float convert(char *entCurrency, char *destCurrency, float amount)
{
	float val = 0;
	float usdBuffer = 0;
	// Convert to USD first.
	if (strcmp(entCurrency, "CLP") == 0 || strcmp(entCurrency, "clp") == 0)
	{
		if (amount < exchangeRates.clpMin)
		{
			val = -1.0;
		}
		else
		{
			if (amount > exchangeRates.clpMax)
			{
				val = -2.0;
			}
			else
			{

				usdBuffer = amount * exchangeRates.clp;
			}
		}
	}
	else
	{
		if (strcmp(entCurrency, "ARS") == 0 || strcmp(entCurrency, "ars") == 0)
		{
			if (amount < exchangeRates.arsMin)
			{
				val = -1.0;
			}
			else
			{
				if (amount > exchangeRates.arsMax)
				{
					val = -2.0;
				}
				else
				{

					usdBuffer = amount * exchangeRates.ars;
				}
			}
		}
		else
		{
			if (strcmp(entCurrency, "USD") == 0 || strcmp(entCurrency, "usd") == 0)
			{
				if (amount < exchangeRates.usdMin)
				{
					val = -1.0;
				}
				else
				{
					if (amount > exchangeRates.usdMax)
					{
						val = -2.0;
					}
					else
					{

						usdBuffer = amount * exchangeRates.usd;
					}
				}
			}
			else
			{
				if (strcmp(entCurrency, "EUR") == 0 || strcmp(entCurrency, "eur") == 0)
				{
					if (amount < exchangeRates.eurMin)
					{
						val = -1.0;
					}
					else
					{
						if (amount > exchangeRates.eurMax)
						{
							val = -2.0;
						}
						else
						{
							usdBuffer = amount * exchangeRates.eur;
						}
					}
				}
				else
				{
					if (strcmp(entCurrency, "TRY") == 0 || strcmp(entCurrency, "try") == 0)
					{
						if (amount < exchangeRates.tryMin)
						{
							val = -1.0;
						}
						else
						{
							if (amount > exchangeRates.tryMax)
							{
								val = -2.0;
							}
							else
							{

								usdBuffer = amount * exchangeRates.try;
							}
						}
					}
					else
					{
						if (strcmp(entCurrency, "GBP") == 0 || strcmp(entCurrency, "gbp") == 0)
						{
							if (amount < exchangeRates.gbpMin)
							{
								val = -1.0;
							}
							else
							{
								if (amount > exchangeRates.gbpMax)
								{
									val = -2.0;
								}
								else
								{

									usdBuffer = amount * exchangeRates.gbp;
								}
							}
						}
					}
				}
			}
		}
	}
	// Convert to desired currency
	if (val >= 0)
	{
		if (strcmp(destCurrency, "ARS") == 0 || strcmp(destCurrency, "ars") == 0)
		{
			val = usdBuffer / exchangeRates.ars;
			if (val < exchangeRates.arsMin)
			{
				val = -3.0;
			}
			else
			{
				if (val > exchangeRates.arsMax)
				{
					val = -4.0;
				}
			}
		}
		else
		{
			if (strcmp(destCurrency, "CLP") == 0 || strcmp(destCurrency, "CLP") == 0)
			{
				val = usdBuffer / exchangeRates.clp;
				if (val < exchangeRates.clpMin)
				{
					val = -3.0;
				}
				else
				{
					if (val > exchangeRates.clpMax)
					{
						val = -4.0;
					}
				}
			}
			else
			{
				if (strcmp(destCurrency, "USD") == 0 || strcmp(destCurrency, "usd") == 0)
				{
					val = usdBuffer / exchangeRates.usd;
					printf("val usd es %f\n", val);
					if (val < exchangeRates.usdMin)
					{
						val = -3.0;
					}
					else
					{
						if (val > exchangeRates.usdMax)
						{
							val = -4.0;
						}
					}
				}
				else
				{
					if (strcmp(destCurrency, "EUR") == 0 || strcmp(destCurrency, "eur") == 0)
					{
						val = usdBuffer / exchangeRates.eur;
						if (val < exchangeRates.eurMin)
						{
							val = -3.0;
						}
						else
						{
							if (val > exchangeRates.eurMax)
							{
								val = -4.0;
							}
						}
					}
					else
					{
						if (strcmp(destCurrency, "TRY") == 0 || strcmp(destCurrency, "try") == 0)
						{
							val = usdBuffer / exchangeRates.try;
							if (val < exchangeRates.tryMin)
							{
								val = -3.0;
							}
							else
							{
								if (val > exchangeRates.tryMax)
								{
									val = -4.0;
								}
							}
						}
						else
						{
							if (strcmp(destCurrency, "GBP") == 0 || strcmp(destCurrency, "gbp") == 0)
							{
								val = usdBuffer / exchangeRates.ars;
								if (val < exchangeRates.gbpMin)
								{
									val = -3.0;
								}
								else
								{
									if (val > exchangeRates.gbpMax)
									{
										val = -4.0;
									}
								}
							}
						}
					}
				}
			}
		}
	}
	return val;
}

int main()
{
	printf("Welcome to the RBank currency converter\n");
	printf("-----------------------------------\n");
	char currency[10] = "";
	char currencyDest[10] = "";
	float amount = 0;
restart:
	while (1)
	{
		if (firstEntry)
		{
			printf("-> Please input your initial currency(CLP, ARS, USD, EUR, TRY, GBP): ");
			fflush(stdin);
			scanf("%s", currency);
		}
		if (firstEntry)
		{
			printf("-> Introduce amount you wish to convert: ");
			fflush(stdin);
			scanf("%f", &amount);
			firstEntry = false;
		}
	opt2:
		// Once you added the funds to exchange you can access the other options
		printf("-> Input secondary currency: ");
		fflush(stdin);
		scanf("%s", currencyDest);
		float cv = convert(currency, currencyDest, amount);
		amount = cv;
		printf("----------------------------------\n");

		if (amount == -1)
		{
			printf("-> Amount for %s lower than the minimum permitted for currency conversion\n", currency);
		}
		else
		{
			if (amount == -2)
			{
				printf("-> Amount for %s higher than the maximum permitted for currency conversion\n", currency);
			}
			else
			{
				if (amount == -3)
				{
					printf("-> Amount for %s lower than the minimum permitted for currency conversion\n", currencyDest);
				}
				else
				{
					if (amount == -4)
					{
						printf("-> Amount for %s higher than the maximum permitted for currency conversion\n", currencyDest);
					}
					else
					{
						strcpy(currency, currencyDest);
						while (true)
						{
							int cas = 0;
							printf("-> Input 1 to withdraw your funds?\n");
							printf("-> Input 2 to convert your current funds to another currency?\n");
							printf("-> Input 3 to restart the system \n");
							printf("-> Input 4 to exit the system\n");
							printf("-> Input 5 to check your current funds and currency\n");
							printf("-> Select an option: ");
							fflush(stdin);
							scanf("%d", &cas);
							switch (cas)
							{
							case 1:
								float fee = cv * 0.1;
								cv = cv - fee;
								printf("----------------------------------\n");
								printf("-> Withdrawing %f in %s\n", amount, currency);
								amount = 0;
								printf("-> Current amount of funds: %f\n", amount);
								printf("----------------------------------\n");
								break;

							case 2:
								printf("----------------------------------\n");
								printf("Your current amount is: %f %s\n", amount, currency);
								goto opt2;
								break;

							case 3:
								printf("----------------------------------\n");
								printf("Restarting system\n");
								firstEntry = true;
								goto restart;
								break;

							case 4:
								goto exit;
								break;
							case 5:
								printf("----------------------------------\n");
								printf("-> Current amount of funds: %f and currency %s\n", amount, currency);
								printf("----------------------------------\n");
								break;
							}
						}
					}
				}
			}
		}
	}
exit:
	return 0;
}