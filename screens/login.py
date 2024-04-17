from sqlite3 import IntegrityError
import flet as ft
from database import PasswordVault

class LoginScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        def gotoVault(vault):

            vault = PasswordVault(password.value)
            try:
                vault.login_user(username.value, password.value)
                page.go('/vault')
            except:
                page.dialog = ft.AlertDialog(
                    modal=True,
                    content=ft.Text('Invalid username or password.'),
                    actions=[ft.ElevatedButton(text='Okay')]
                )


        username = ft.TextField(label='Username', width= 150)
        password = ft.TextField(label='Password', width= 150)
        self.content=ft.Column(
            controls=[
                ft.Text("Login Screen"),
                username,
                password,
                ft.ElevatedButton(text='Login', on_click= gotoVault),
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ]
        )
