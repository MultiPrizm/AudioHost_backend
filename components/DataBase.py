import dotenv, os, hashlib, colorama, components.logger, sys

import mysql
import mysql.connector

dotenv.load_dotenv()

class MSDB():
    try:
        db = mysql.connector.connection.MySQLConnection(
            user=os.getenv("DB_USER"), 
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB"),
            auth_plugin='caching_sha2_password'
        )

        cursor = db.cursor()
        print("MSDB[", colorama.Fore.GREEN + "OK",colorama.Style.RESET_ALL + "]: database connected.")

    except Exception as e:
        print("MSDB[", colorama.Fore.RED + "ERROR",colorama.Style.RESET_ALL + "]: database connect fail.")
        components.logger.error(e)

    def reg_new_user(self, login: str, password: str):

        self.cursor.execute("SELECT * FROM users WHERE login = %s", (login,))

        res = self.cursor.fetchall()

        if 0 != len(res):
            return False

        self.cursor.execute("INSERT INTO users (login, password, usertype) VALUES (%s, %s, %s)", (login, hashlib.sha256(password.encode()).hexdigest(), "user"))
        self.db.commit()
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
    
    def get_popular_audio(self, page = 1):

        self.cursor.execute("SELECT * FROM popularSongs LIMIT 5 OFFSET %s", ((page - 1) * 5,))

        songs_id = self.cursor.fetchall()

        songs_id_list = []
        songs_list = []

        for i in songs_id:
            songs_id_list.append(i[0])
        
        for i in songs_id_list:

            self.cursor.execute("SELECT download_endpoint FROM audiolist WHERE id = %s", (int(i),))
            songs_list.append(self.cursor.fetchall())
        
        return songs_list

    