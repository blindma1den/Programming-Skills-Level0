use reqwest::{Url, header::Keys};
use mini_redis::Result;
use crate::currency_converter;
use std::{fmt, collections::HashMap};
use serde::Deserialize;


impl fmt::Display for currency_converter::Currency {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            currency_converter::Currency::CLP => write!(f, "CLP"),
            currency_converter::Currency::ARS => write!(f, "ARS"),
            currency_converter::Currency::USD => write!(f, "USD"),
            currency_converter::Currency::EUR => write!(f, "EUR"),
            currency_converter::Currency::GBP => write!(f, "GBP"),
            currency_converter::Currency::TRY => write!(f, "TRY"),
        }
    }
}

#[derive(Deserialize)]
struct Response {
    data: HashMap<Option<currency_converter::Currency>,f32>
}

pub async fn latest(
    from: currency_converter::Currency,
    to: currency_converter::Currency,
) -> Result<f32> {
    let key = to.clone();
    let from_str = from.to_string();
    let from = from_str.as_str();
    let to_str = to.to_string();
    let to = to_str.as_str();
    let params = [
        (
            "apikey",
            "fca_live_ENNltxSjPmYko08L7BtMls2AyDJwulmpwLwikx48",
        ),
        ("base_currency", from),
        ("currencies", to),
    ];
    let url = Url::parse_with_params("https://api.freecurrencyapi.com/v1/latest", &params).unwrap();
    let resp = reqwest::get(url).await?.json::<Response>().await?;
    let rate = resp.data.get(&Some(key)).unwrap();

    Ok(rate.to_owned())
}
