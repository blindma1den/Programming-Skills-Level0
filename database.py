import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cursor = self.conn.cursor()
      
    def close_connection(self):
        self.conn.close()

    def create_tables(self):
        _ = self.cursor.execute('select name from sqlite_master')
        result = _.fetchall()
        if len(result) == 0:
            self.cursor.execute("""create table account(
                                first_name varchar(50), 
                                last_name varchar(50), 
                                password varchar(50), 
                                amount integer not null,
                                intentos int default 0 not null,
                                bloqueo boolean default false not null
                                )
                                """)
        
            # INSERTAR USUARIOS DEFAULT
            self.cursor.execute("""insert into account values
                                ('admin', 'admin', 'admin', 2000, 0, false),
                                ('default', 'user', 'admin', 2500, 0, false)
                                """)
        self.conn.commit()
        self.close_connection()

    def insert(self, insertion):
        self.cursor.execute(insertion)
        self.conn.commit()

    def updated(self, upgrade):
        self.cursor.execute(upgrade)
        self.conn.commit()

    def query(self, query):
        _query = self.cursor.execute(query)
        result = _query.fetchall()
        return result
      
    def tries(self):
        pass
    
    
class User:
    first_name = None
    last_name = None
    password = None
    amount = 2000
    def connect_database(self):
        connect = Database()
        return connect
    
    def create_user(self, first_name, last_name, password):
        self.cursor.execute(f"insert into account values('{first_name}', '{last_name}', '{password}', 2000)")
        self.conn.commit()
        self.close()
      
    def deposit(self, deposit):
        new_amount = int(self.amount) + int(deposit)
        updated = f"update account set amount = {new_amount} where first_name = '{self.first_name}'"
        conn = self.connect_database()
        conn.updated(updated)
        conn.close_connection()
        self.amount = new_amount
        return new_amount
    
    def withdraw(self, withdraw):
        new_amount = int(self.amount) - int(withdraw)
        if new_amount < 0:
            return ValueError('El monto a retirar supera lo que estâ depositado')
        updated = f"update account set amount = {new_amount} where first_name = '{self.first_name}'"
        conn = self.connect_database()
        conn.updated(updated)
        conn.close_connection()
        self.amount = new_amount
        return self.amount
    
    def view(self):
        return self.amount
      
      
    def transfer_money(self, transferir_a, monto):
        conn = self.connect_database()
        _ = conn.query(f'select first_name from account where first_name != "{self.first_name}"')
        _transferir_a = _[0][int(transferir_a) - 1]
        nuevo_monto_propio = int(self.amount) - int(monto)
        conn.updated(f'update account set amount = {nuevo_monto_propio} where first_name = "{self.first_name}"')
        self.amount = nuevo_monto_propio    
        transferencia = conn.query(f'select amount from account where first_name = "{_transferir_a}"')
        nuevo_monto_tercero = int(transferencia[0][0]) + int(monto)
        conn.updated(f'update account set amount = {nuevo_monto_tercero} where first_name = "{_transferir_a}"')
        return self.amount


    def users(self):
        conn = self.connect_database()
        _query = conn.query(f'select first_name from account where first_name != "{self.first_name}"')
        return _query

      
    def login(self, username, password):
      
        conn = self.connect_database()
        query = conn.query(f'select * from account where first_name = "{username}"')
        
        if query:
            result = query[0]
            
            if result[4] >= 3:
                print('\n-'*50)
                print('USUARIO BLOQUEADO')
                print('POR AHORA NO CONTAMOS CON LA OPCION DE RECUPERAR USUARIO, ESPERE LA ACTUALIZACION DEL SISTEMA')
                return False

            if result[2] == password:
                self.first_name = result[0]
                self.last_name = result[1]
                self.password = result[2]
                self.amount = result[3]
                self.intentos = result[4]
                conn.close_connection()
                return True
            else:
                intentos = int(result[4]) + 1
                conn.updated(f'update account set intentos = {intentos} where first_name = "{result[0]}"')
                print('\n-'*50,'SU USUARIO HA SIDO BLOQUEADO AL FALLAR 3 VECES') if intentos > 2 else None
                conn.close_connection()
        return False
