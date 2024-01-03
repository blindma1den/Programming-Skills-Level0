package main

import (
	"errors"
	"fmt"

	"example.com/bank/auth"
	"example.com/bank/data"
	"example.com/bank/input"
	"example.com/bank/user"
)

func main() {
	input.WelcomeUser()

	users := data.GetData()
	user, err, _ := authenticateUser(users)

	if err != nil {
		fmt.Printf("ERROR: %v", err)
		return
	}

	for {
		user.ResetFailedLoginAttempts()
		input.PresentOptions()
		choice := input.GetChoice()

		switch choice {

		case 1:
			accountBalance := user.BankAccount.GetBalance()
			fmt.Printf("Your balance is %g\n\n", accountBalance)

		case 2:
			amount := input.GetAmount("Enter the deposit amount: ")
			user.BankAccount.Deposit(amount)
			fmt.Printf("Balance updated! New amount: %g\n\n", user.BankAccount.GetBalance())

		case 3:
			amount := input.GetAmount("Enter the withdrawal amount: ")
			if amount > user.BankAccount.GetBalance() {
				fmt.Printf("Invalid amount. You can't withdraw more than you have.\n\n")
				continue
			}

			user.BankAccount.Withdraw(amount)
			fmt.Printf("Balance updated! New amount: %g\n\n", user.BankAccount.GetBalance())

		case 4:
			recipientUsername := input.GetText("Enter the recipient's username: ")
			recipientUser, err := getUser(users, recipientUsername)
			if err != nil {
				fmt.Printf("User %s could not be found\n\n", recipientUsername)
				continue
			}

			amount := input.GetAmount("Enter the transfer amount: ")
			user.BankAccount.Withdraw(amount)
			recipientUser.BankAccount.Deposit(amount)

			fmt.Printf("New balance for user %s: %g\n", user.Username, user.BankAccount.GetBalance())
			fmt.Printf("New balance for user %s: %g\n\n", recipientUsername, recipientUser.BankAccount.GetBalance())

		default:
			fmt.Println("Goodbye!")
			return
		}

	}

}

func getUser(users map[string]*user.User, username string) (*user.User, error) {
	user, exists := users[username]

	if !exists {
		return nil, errors.New("User not found")
	}

	return user, nil
}

func authenticateUser(users map[string]*user.User) (*user.User, error, bool) {
	var user *user.User
	var err error

	for {
		username := input.GetText("Enter your username: ")
		password := input.GetText("Enter your password: ")

		user, err = getUser(users, username)
		if err != nil {
			return nil, errors.New("User not found"), false
		}

		err = auth.Login(user, password)
		if err != nil {
			fmt.Printf("Invalid credentials.\n\n")

			user.IncreaseFailedLoginAttempts()
			if user.ShouldBeLockedOut() {
				return user, errors.New("The maximum number of failed login attempts has been reached. The user has been locked out."), true
			}

			continue
		}

		break
	}

	return user, nil, false
}
