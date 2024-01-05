use std::io::stdin;

pub struct Response {
  pub message: String,
  pub success: bool,
 }
struct User {
  online: bool,
  username: &'static str,
  password: &'static str,
  balance: u32,
  lock: u64,
}


trait System {
  fn new(username: &'static str, password: &'static str) -> Self;
}

impl User {
  fn set_usr_online(&mut self) {
    self.online = true
  }
  fn mark_wrong_user(&mut self) {
    self.lock += 1;
  }

  fn log_in(&mut self, usr: &str, psw: &str) -> Response {
    if usr.trim() == self.username && psw.trim() != self.password {
      if self.lock == 2 {
        self.mark_wrong_user();
        Response {
          message: "user locked".to_owned(),
          success: false,
        }
      } else {
        self.mark_wrong_user();
        Response {
          message: "password does not match".to_owned(),
          success: false,
        }
      }
    } else if usr.trim() == self.username && psw.trim() == self.password {
      self.set_usr_online();
      Response {
        message: "usr logged in".to_owned(),
        success: true,
      }
    } else {
      Response {
        message: "user not found".to_owned(),
        success: false,
      }
    }
  }

  fn log_out(&mut self) {
    self.online = false;
  }

  fn withdraw(&mut self, amount: f32) -> Response {
    let amount_u32 = amount as u32;
    if amount_u32 > self.balance {
      Response {
        message: "insufficient funds".to_owned(),
        success: false,
      }
    } else if amount_u32 > 0 {
      self.balance -= amount_u32;
      Response {
        message: "withdraw successful".to_owned(),
        success: true,
      }
    } else {
      Response {
        message: "withdraw only positive amount".to_owned(),
        success: false,
      }
    }
  }
  fn transfer(&mut self, amount: f32, destination: &str) -> Response {
    let amount_u32 = amount as u32;
    if amount_u32 > self.balance {
      Response {
        message: "insufficient funds".to_owned(),
        success: false,
      }
    } else if amount_u32 > 0 {
      println!("transferring to {}", destination);
      self.balance -= amount_u32;

      Response {
        message: "transference successful".to_owned(),
        success: true,
      }
    } else {
      Response {
        message: "transfer only positive amount".to_owned(),
        success: false,
      }
    }
  }
  fn deposit(&mut self, amount: f32) -> Response {
    let amount_u32 = amount as u32;
    if amount_u32 > 0 {
      self.balance += amount_u32;
      Response {
        message: "deposit successful".to_owned(),
        success: true,
      }
    } else {
      Response {
        message: "deposit only positive amount".to_owned(),
        success: false,
      }
    }
  }
  fn check_balance(&self) -> u32 {
    self.balance
  }
  fn display_menu(&mut self) {
    let mut menu = String::new();
    println!("choose an option to perform: ");
    println!("1 - view balance");
    println!("2 - withdraw");
    println!("3 - deposit");
    println!("4 - transfer");
    println!("0 - exit");

    stdin().read_line(&mut menu).expect("Failed to read line");
    match menu.trim() {
      "1" => {
        println!("your balance is: {}", self.check_balance());
      }
      "2" => {
        let mut amount = String::new();
        println!("amount to withdraw:");
        stdin().read_line(&mut amount).expect("Failed to read line");
        let Response {
          message,
          success: _,
        } = self.withdraw(amount.trim().parse::<f32>().unwrap());
        println!("{}", message);
      }
      "3" => {
        let mut amount = String::new();
        println!("amount to deposit:");
        stdin().read_line(&mut amount).expect("Failed to read line");
        let Response {
          message,
          success: _,
        } = self.deposit(amount.trim().parse::<f32>().unwrap());
        println!("{}", message);
      }
      "4" => {
        //transfer
        let mut destination = String::new();
        println!("destination account:");
        stdin()
          .read_line(&mut destination)
          .expect("Failed to read line");
        let mut amount = String::new();
        println!("amount to transfer:");
        stdin().read_line(&mut amount).expect("Failed to read line");
        let Response {
          message,
          success: _,
        } = self.transfer(amount.trim().parse::<f32>().unwrap(), destination.trim());
        println!("{}", message);
      }
      "0" => {
        self.log_out();
        println!("exit from bank system");
      }
      _ => {
        println!("Unavailable option");
      }
    }
  }
}

impl System for User {
  fn new(username: &'static str, password: &'static str) -> User {
    User {
      username,
      password,
      balance: 2000,
      lock: 0,
      online: false,
    }
  }
}

pub fn main() {
  let mut bank: User = System::new("usr", "psw");
  println!("{} - {}", bank.username, bank.password);
  let mut username = String::new();
  println!("log in system");

  println!("username:");
  stdin()
    .read_line(&mut username)
    .expect("Failed to read line");

  while !bank.online & (bank.lock != 3) {
    let mut password = String::new();

    println!("password:");
    stdin()
      .read_line(&mut password)
      .expect("Failed to read line");

    let Response { message, success } = bank.log_in(username.as_str(), password.as_str());

    match (success, message.as_str()) {
      (false, "user locked") => {
        println!("{}, exit from system", message);
      }
      (true, "usr logged in") => {
        println!("welcome to bank system - {}", bank.username);
      }
      (false, "password does not match") => {
        println!("{} - retry", message);
      }
      (false, "user not found") => {
        username = String::new();
        println!("{} - ...", message);
        println!("username:");
        stdin()
          .read_line(&mut username)
          .expect("Failed to read line");
      }
      (_, _) => {
        "out of system".to_string();
      }
    }
  }

  while bank.online {
    bank.display_menu()
  }
}
