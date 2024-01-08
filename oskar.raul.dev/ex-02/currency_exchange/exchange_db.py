import csv
import os

CSV_DATABASE_EXCHANGE_FILE_NAME = 'db.csv'

# init database
CSV_EXCHANGE_TABLE = None
AVAILABLE_CURRENCIES = None

def available_currencies():
  global AVAILABLE_CURRENCIES
  return AVAILABLE_CURRENCIES

def csv_exchange_table():
  global CSV_EXCHANGE_TABLE
  return CSV_EXCHANGE_TABLE

def load_csv_db():
  global AVAILABLE_CURRENCIES
  global CSV_EXCHANGE_TABLE
  
  # load absolute path of csv file
  directory=os.path.dirname(__file__)
    
  with open(os.path.join(directory, CSV_DATABASE_EXCHANGE_FILE_NAME)) as db:
    CSV_EXCHANGE_TABLE = {}
    AVAILABLE_CURRENCIES = []
    reader = csv.reader(db, delimiter=',')
    for row in reader:
      if not row[0] in AVAILABLE_CURRENCIES:
        AVAILABLE_CURRENCIES.append(row[0])
      if not row[0] in CSV_EXCHANGE_TABLE:
        CSV_EXCHANGE_TABLE[row[0]] = {}
      CSV_EXCHANGE_TABLE[row[0]][row[1]]  = float(row[2])
    # sort currency list for better presentation
    AVAILABLE_CURRENCIES.sort()
    