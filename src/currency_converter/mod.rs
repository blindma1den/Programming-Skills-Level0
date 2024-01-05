mod currency_service;
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
      _ => Err("no matched currency").unwrap(),
    }
  }
}

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
  fn withdraw() -> () {}
}

impl System for Exchange {
  async fn new(from: Currency, to: Currency) -> Result<Exchange> {
    match from {
      Currency::ARS => Ok(Exchange {
        from,
        to,
        max: 3e6,
        min: 1000.00,
        rate: 1000.00,
      }),
      Currency::CLP => Ok(Exchange {
        from,
        to,
        max: 3e6,
        min: 1000.00,
        rate: 1000.00,
      }),
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
      Currency::USD => {
        let rate = get_rate(from.clone(), to.clone()).await?;
        Ok(Exchange {
          from,
          to,
          max: 3000.00,
          min: 1.00,
          rate,
        })
      }
    }
  }
}

pub async fn main() -> Result<()> {
  println!("currency converter");
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

  println!("rate - {:?}", system?.rate);

  Ok(())
}
