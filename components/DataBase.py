import dotenv, os, hashlib

from mysql.connector import connection

dotenv.load_dotenv()

class MSDB():

    db = connection.MySQLConnection(
        user=os.getenv("DB_USER"), 
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB")
    )

    cursor = db.cursor()

    def reg_new_user(self, login: str, password: str):

        self.cursor.execute("SELECT * FROM users WHERE login = %s", (login,))

        res = self.cursor.fetchall()

        if 0 != len(res):
            return False

        self.cursor.execute("INSERT INTO users (login, password, usertype) VALUES (%s, %s, %s)", (login, hashlib.sha256(password.encode()).hexdigest(), "user"))

        return True
    
    def login_user(self, login: str, password: str):

        self.cursor.execute("SELECT * FROM users WHERE login = %s", (login,))

        res = self.cursor.fetchall()

        if not res:
            return False
        
        if res[0][1] == hashlib.sha256(password.encode()).hexdigest():
            return True
        else: 
            return False