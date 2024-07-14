import os, dotenv, hashlib
from itsdangerous import URLSafeSerializer

dotenv.load_dotenv()

class AppCryptographer():

    def __init__(self, active: bool = True) -> None:

        self.__ac = URLSafeSerializer(os.getenv("SECRET_KEY"))
        self.__active = active
        self.__hash_key = hashlib.sha256(os.getenv("SECRET_KEY").encode())

    def get_hash_key(self):

        return self.__hash_key

    def encrypt(self, arg: str):

        if self.__active:
            return self.__ac.dumps(arg)
        else:
            return arg
    
    def decrypt(self, arg: str, hash_key: str):

        if hash_key == self.__hash_key:
            return self.__ac.loads(arg, max_age=3600)
        else:
            return False