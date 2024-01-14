mod currency_service;
use crate::Response;
use mini_redis::Result;
use serde::{Deserialize, Serialize};
use std::io::stdin;

//derive clone para currency
#[derive(Deserialize, Serialize, Eq, PartialEq, Hash, Clone)]
pub enum Currency {
  CLP,
  ARS,
  USD,
  EUR,
  TRY,
  GBP,
}

impl Currency {
  fn from_str(s: &str) -> Currency {
    match s.trim() {
      "CLP" => Currency::CLP,
      "ARS" => Currency::ARS,
      "USD" => Currency::USD,
      "EUR" => Currency::EUR,
      "TRY" => Currency::TRY,
      "GBP" => Currency::GBP,
      _ => panic!("{:?}", "no matched currency"),
    }
  }
}

#[derive(Clone, Deserialize, Serialize)]
struct Exchange {
  from: Currency,
  to: Currency,
  min: f32,
  max: f32,
  rate: f32,
}

async fn get_rate(from: Currency, to: Currency) -> Result<f32> {
  let res = currency_service::latest(from, to).await?;
  println!("data {}", res);
  Ok(res)
}

trait System {
  async fn new(from: Currency, to: Currency) -> Result<Exchange>;
}

impl Exchange {
  fn withdraw(&mut self, amount: f32) -> Response {
    let gross = amount * self.rate;

    return match (gross > self.max, gross < self.min) {
      (true, _) => Response {
        message: "the amount is greater than the maximum allowed".to_owned(),
        success: false,
      },
      (_, true) => Response {
        message: "the amount is less than the minimum allowed".to_owned(),
        success: false,
      },
      _ => {
        //mock some system to withdraw
        //
        let net = gross - (gross * 0.01);
        let net_ref = net;
        println!("net - {}", net);
        let from = self.from.to_string();
        let from_ref = from.as_str();

        let to = self.to.to_string();
        let to_ref = to.as_str();
        let message = format!(
          "withdrawn {} {} from {} balance - (1% commission)",
          net_ref, to_ref, from_ref
        );
        Response {
          message,
          success: true,
        }
      }
    };
  }
}

impl System for Exchange {
  async fn new(from: Currency, to: Currency) -> Result<Exchange> {
    match to {
      Currency::ARS => {
        let rate = get_rate(from.clone(), Currency::USD).await?;
        Ok(Exchange {
          from,
          to,
          max: 200e6,
          min: 1000.00,
          rate: rate * 1000.00,
        })
      }
      Currency::CLP => {
        let rate = get_rate(from.clone(), Currency::USD).await?;
        Ok(Exchange {
          from,
          to,
          max: 200e6,
          min: 1000.00,
          rate: rate * 1000.00,
        })
      }
      Currency::EUR => {
        let rate = get_rate(from.clone(), to.clone()).await?;
        Ok(Exchange {
          from,
          to,
          max: 3000.00,
          min: 1.0,
          rate,
        })
      }
      Currency::GBP => {
        let rate = get_rate(from.clone(), to.clone()).await?;
        Ok(Exchange {
          from,
          to,
          max: 2400.00,
          min: 0.8,
          rate,
        })
      }
      Currency::TRY => {
        let rate = get_rate(from.clone(), to.clone()).await?;
        Ok(Exchange {
          from,
          to,
          max: 89000.00,
          min: 29.9,
          rate,
        })
      }
      Currency::USD => match from {
        Currency::ARS => Ok(Exchange {
          from,
          to,
          max: 3000.00,
          min: 1.00,
          rate: 0.001,
        }),
        Currency::CLP => Ok(Exchange {
          from,
          to,
          max: 3000.00,
          min: 1.00,
          rate: 0.001,
        }),
        _ => {
          let rate = get_rate(from.clone(), to.clone()).await?;
          Ok(Exchange {
            from,
            to,
            max: 3000.00,
            min: 1.00,
            rate,
          })
        }
      },
    }
  }
}

pub async fn main() -> Result<()> {
  let mut menu = String::from("on");
  println!("currency converter");
  while menu == "on" {
    let mut from = String::new();
    let mut to = String::new();
    println!("from: ");

    stdin().read_line(&mut from).expect("Failed to read line");
    println!("to: ");
    stdin().read_line(&mut to).expect("Failed to read line");
    print!("from: {} to: {}", from, to);
    let system: Result<Exchange> =
      Ok(<Exchange as System>::new(Currency::from_str(&from), Currency::from_str(&to)).await?);

    if system.is_err() {
      println!("error: {}", system.err().unwrap());
      return Ok(());
    }

    let mut system_clone = system?.clone();

    println!("do you want to withdraw? y/n");
    let mut answer = String::new();
    stdin().read_line(&mut answer).expect("Failed to read line");
    match answer.trim() {
      "y" => {
        let mut amount = String::new();
        println!("amount to withdraw:");
        stdin().read_line(&mut amount).expect("Failed to read line");

        let Response {
          message,
          success: _,
        } = system_clone.withdraw(amount.trim().parse::<f32>().unwrap());
        println!("{}", message);
      }
      "n" => {
        println!("exit from exchange system");
        menu = "off".to_string();
      }
      _ => {
        println!("Unavailable option");
      }
    }

    println!("do you want to perform another operation? y/n");
    let mut session = String::new();
    stdin()
      .read_line(&mut session)
      .expect("Failed to read line");
    match session.trim() {
      "y" => {
        println!("choose your currency");
      }
      "n" => {
        println!("exit from exchange system");
        menu = "off".to_string();
      }
      _ => {
        println!("Unavailable option");
      }
    }
  }

  Ok(())
}
