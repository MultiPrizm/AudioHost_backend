import dotenv, os, hashlib, colorama, components.logger, sys, json

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

        self.cursor.execute("INSERT INTO users (login, password, usertype, playlist) VALUES (%s, %s, %s, %s)", (login, hashlib.sha256(password.encode()).hexdigest(), "user", json.dumps({"1": []})))
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
        try:
            self.cursor.execute("SELECT * FROM popularSongs LIMIT 5 OFFSET %s", ((page - 1) * 5,))

            songs_id = self.cursor.fetchall()

            songs_id_list = []
            songs_list = []

            for i in songs_id:
                songs_id_list.append(i[0])
            
            for i in songs_id_list:

                self.cursor.execute("SELECT * FROM audiolist WHERE id = %s", (int(i),))
                songs_list.append(self.cursor.fetchall())
            
            return songs_list
        except Exception as e:
            components.logger.error(e)

            return []
        
    def get_playlist(self, login):

        try:
            self.cursor.execute("SELECT playlist FROM users WHERE login = %s", (login,))
            res = self.cursor.fetchall()
            res = json.loads(res[0][0])
            return res["1"]

        except Exception as e:
            components.logger.error(e)

            return []
    
    def update_playlist(self, _list: list, login: str) -> bool:
        try:
            # Перевірка типу _list
            if not isinstance(_list, list):
                raise TypeError("Expected _list to be of type list")

            # Перетворення списку в JSON-рядок
            playlist = {"1": _list}
            playlist_json = json.dumps(playlist)  # Це має бути рядок JSON

            # Виконання запиту
            self.cursor.execute(
                "UPDATE users SET playlist = %s WHERE login = %s",
                (playlist_json, login)
            )
            self.db.commit()

            return True

        except Exception as e:
            components.logger.error("Error updating playlist: %s", e)
            return False
    
    def get_tracks_from_id(self, idlist: list):

        tracklist = []

        for i in idlist:

            self.cursor.execute("SELECT * FROM audiolist WHERE id = %s", (int(i),))
            tracklist.append(self.cursor.fetchall())
        
        return tracklist

    