package auth

import (
	"errors"

	"example.com/bank/user"
)

func Login(user *user.User, password string) error {
	if password != user.Password {
		return errors.New("Credentials invalid")
	}

	return nil
}
