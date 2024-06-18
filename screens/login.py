import flet as ft
from database import PasswordVault

class LoginScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.username = ft.TextField(label='Username', width= 150)
        self.password = ft.TextField(label='Password', width= 150)
        self.content=ft.Column(
            controls=[
                ft.Text("Login Screen"),
                self.username,
                self.password,
                ft.ElevatedButton(text='Login', on_click= lambda _: self.login(page, self.username.value, self.password.value)),
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ]
        )

    def login(self, page: ft.Page, username, password):
        vault = PasswordVault(password)
        if vault.login_user(username, password):
            self.vault = vault
            page.go('vault')
        else:
            password.error_text = "Invalid username or password. Try again."
            page.update()

