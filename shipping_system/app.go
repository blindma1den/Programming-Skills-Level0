package main

import (
	"fmt"
	"log"
	"net/http"
	"html/template"	
)

type User struct {
	ID uint `json:"id"`
	Username string `json:"username"`
	Password string `json:"password"`
	LoginAttempts int `json:"loginAttempts"`
}


var users = make(map[string]*User)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World, Ilove %s", r.URL.Path[1:])
}

func register(w http.ResponseWriter, r *http.Request) {
	var user User
	if r.Method == http.MethodPost {
		username := r.FormValue("username")
		password := r.FormValue("password")
		// Check if username already exists
		if _, ok := users[username]; ok {
			http.Error(w, "Username already exists", http.StatusBadRequest)
			fmt.Println("Username already exists")
			return
		}
		user.Username = username
		user.Password = password
		user.LoginAttempts = 0
		users[user.Username] = &user
		http.Redirect(w, r, "/login", http.StatusSeeOther)
		fmt.Println("User registered successfully", users)
	}
	tmpl, err := template.ParseFiles("templates/register.html")
	if err != nil {
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

func login(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodPost {
		username := r.FormValue("username")
		password := r.FormValue("password")
		if user, ok := users[username]; ok {
			if user.Password == password{
				user.LoginAttempts = 0
				http.Redirect(w, r, "/", http.StatusSeeOther)
			} else {
				user.LoginAttempts++
				http.Error(w, "Invalid username or password", http.StatusUnauthorized)
				fmt.Println("Invalid username or password")
				if user.LoginAttempts > 3 {
					http.Error(w, "Too many failed login attempts, user is blocked", http.StatusUnauthorized)
					fmt.Println("User is blocked", user)
					return
				}
				return
			}	
		}
		http.Error(w, "User not found", http.StatusUnauthorized)
		fmt.Println("User not found")
	}
	tmpl, err := template.ParseFiles("templates/login.html")
	if err != nil {
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, nil)
}

func main(){
	http.HandleFunc("/", handler)
	http.HandleFunc("/register", register)
	http.HandleFunc("/login", login)
	
	log.Fatal(http.ListenAndServe(":8080", nil))
}