package user

import (
	"example.com/bank/bankaccount"
)

type User struct {
	Username            string
	Password            string
	BankAccount         *bankaccount.BankAccount
	failedLoginAttempts int
}

func New(username string, password string, bankAccount *bankaccount.BankAccount) *User {
	return &User{
		Username:            username,
		Password:            password,
		BankAccount:         bankAccount,
		failedLoginAttempts: 0,
	}
}

func (u *User) GetFailedLoginAttempts() int {
	return u.failedLoginAttempts
}

func (u *User) IncreaseFailedLoginAttempts() {
	u.failedLoginAttempts += 1
}

func (u *User) ResetFailedLoginAttempts() {
	u.failedLoginAttempts = 0
}

func (u *User) ShouldBeLockedOut() bool {
	return u.failedLoginAttempts >= 3
}
