package input

import "fmt"

func WelcomeUser() {
	fmt.Print("Welcome to the online banking system!\n\n")
}

func PresentOptions() {
	fmt.Printf("\nWhat do you want to do?\n")
	fmt.Println("1. Check balance")
	fmt.Println("2. Deposit money")
	fmt.Println("3. Withdraw money")
	fmt.Println("4. Transfer money")
	fmt.Printf("5. Exit\n\n")
}

func GetChoice() int {
	var choice int
	fmt.Print("Your choice: ")
	fmt.Scan(&choice)

	return choice
}

func GetText(message string) string {
	fmt.Print(message)
	var text string
	fmt.Scan(&text)

	return text
}

func GetAmount(message string) float64 {
	fmt.Print(message)
	var amount float64
	fmt.Scan(&amount)

	return amount
}
