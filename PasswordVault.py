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
                       password TEXT)''')
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
    
    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()

        reg_username = ft.TextField(label='Enter your desired username', text_align=ft.TextAlign.LEFT, width=200)
        reg_password = ft.TextField(label='Enter your desired password', text_align=ft.TextAlign.LEFT, width=200)

        page.views.append(
            ft.View(
                route = '/',
                controls = [
                    ft.Text(value='Password Vault', size=30),
                    ft.ElevatedButton(text='Register', on_click=lambda _: page.go('/register')),
                    ft.ElevatedButton(text='Login', on_click= lambda _:page.go('/login'))
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            )    
        )

        if page.route == '/register':
            page.views.append(
                ft.View(
                    route='/register',
                    controls=[
                        ft.Text(value= 'Register', size=30),
                        reg_username,
                        reg_password,
                        ft.ElevatedButton(text='Back Home', on_click= lambda _: page.go('/'))
                    ],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=25
                )
            )
        elif page.route == '/login':
            page.views.append(
                ft.View(
                    route='/login',
                    controls=[
                        ft.Text(value= 'Login', size=30),
                        ft.ElevatedButton(text='Back Home', on_click= lambda _: page.go('/'))
                    ],
                    vertical_alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=25
                )
            )
        page.update()
    
    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)