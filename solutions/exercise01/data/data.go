package data

import (
	"example.com/bank/bankaccount"
	"example.com/bank/user"
)

func GetData() map[string]*user.User {
	return map[string]*user.User{
		"user01": user.New("user01",
			"password01",
			bankaccount.New("1111"),
		),
		"user02": user.New("user02",
			"password02",
			bankaccount.New("2222"),
		),
	}
}
