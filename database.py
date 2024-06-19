import sqlite3
import hashlib
import os

class PasswordVault():
    def __init__(self, master_password):
        self.conn = sqlite3.connect('PV.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password BLOB,
            salt BLOB
        )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS passwords(
            website TEXT,
            username TEXT,
            password BLOB
        )''')
        self.salt = os.urandom(32)
        self.key = hashlib.pbkdf2_hmac('sha256', master_password.encode(), self.salt, 100000)

    def encrypt_password(self, password):
        return hashlib.pbkdf2_hmac('sha256', password.encode(), self.salt, 100000)

    def decrypt_password(self, encrypted_password):
        return encrypted_password.decode()

    def reg_user(self, username, password):
        if self.check_user_exist(username):
            return False


        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        self.c.execute('''INSERT INTO users (
            username,
            password,
            salt
        ) VALUES (?, ?, ?)''', (username, key, salt))
        self.conn.commit()
        
        #return True

    def check_user_exist(self, username):
        self.c.execute("SELECT username FROM users WHERE username=?", (username))
        return bool(self.c.fetchone())

    def login_user(self, username, password):
        self.c.execute('''SELECT password, salt FROM users WHERE username=?''', (username,))
        result = self.c.fetchone()
        if result:
            stored_password, salt = result
            key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
            if key == stored_password:
                return True
        return False

    def save_password(self, website, username, password):
        encrypted_password = self.encrypt_password(password)
        self.c.execute('''
            INSERT INTO passwords(website, username, password)
            VALUES (?, ?, ?)''', (website, username, encrypted_password))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
