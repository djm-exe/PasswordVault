import sqlite3
import hashlib
import flet as ft

class PasswordVault:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('PV.db')
        self.create_table()

    def create_table(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user TEXT,
                       password TEXT''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTEGER,
                       website TEXT,
                       username TEXT,
                       password TEXT,
                       FOREIGN KEYS(user_id) REFERENCES users(id)
        )''')

        self.conn.commit()

    def register(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hashed_password))
        except sqlite3.IntegrityError:
            ...

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False
            

def main(page):
    page.title = "Password Vault"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

    passwordVault = ft.Text(value="Password Vault", color="red")

    page.controls.append(passwordVault)
    page.add(
        ft.ElevatedButton("Register", ft.colors.BLUE_200),
        ft.ElevatedButton("Login", ft.colors.GREEN_200)
    )

ft.app(target=main)