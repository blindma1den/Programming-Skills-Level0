use std::io::stdin;
use mini_redis::Result;
mod bank;
use programming_skills_level0::currency_converter;

#[tokio::main]
async fn main() -> Result<()> {
    println!("select a challenge system:");
    println!("1 - bank");
    println!("2 - currency converter");
    println!("3 - university enrollment");
    println!("4 - online shipping");
    println!("5 - finance management");
    let mut menu = String::new();
    stdin().read_line(&mut menu).expect("Failed to read line");

    match menu.trim() {
        "1" => {
            bank::main();
        }
        "2" => {
            currency_converter::main().await?;
        }
        _ => {
            println!("Unavailable option");
        }
    }

    Ok(())
}
