package bankaccount

const initialBalance = 2000

type BankAccount struct {
	number  string
	balance float64
}

func New(number string) *BankAccount {
	return &BankAccount{
		number:  number,
		balance: initialBalance,
	}
}

func (account *BankAccount) GetBalance() float64 {
	return account.balance
}

func (account *BankAccount) Deposit(amount float64) {
	account.balance += amount
}

func (account *BankAccount) Withdraw(amount float64) {
	account.balance -= amount
}
