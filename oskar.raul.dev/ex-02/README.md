# Excercise 1

## Currency Exchange Database

Currency exchange rates database is located in path

```
currency_exchange/db.csv
```

It is a normal CSV file, each line of the file has three rows. An example line is:

```
USD,ARS,812.00
```

In this line

* First column: Base currency for exchange.
* Second column: Target currency for exchange.
* Third column: exchange Rate

The line is read like: _1 USD is equal to 812.00 ARS_

In the CSV file, for every pair of currencies _A_ and _B_ *must* exists a record for _A_ to _B_ exchange and the _B_ to _A_ exchange as well.

Having a CSV file allows easily adding more currency pairs than the ones mentioned in excersice.

## Running the excercise

To run this excercise you should have Python installed
and execute the following command.


```
python main.py
```

Not aditional dependencies are required.

