import flet as ft
from database import PasswordVault

class LoginScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.vault = PasswordVault('master_password')

        self.error_text = ft.Text(visible=False, color='red')

        self.username = ft.TextField(label='Username', width= 150)
        self.password = ft.TextField(label='Password', width= 150)
        self.content=ft.Column(
            controls=[
                ft.Text("Login Screen"),
                self.username,
                self.password,
                self.error_text,
                ft.ElevatedButton(text='Login', on_click= lambda _: self.login(page)),
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ]
        )

    def login(self, page: ft.Page):
        if self.vault.login_user(self.username.value, self.password.value):
            page.go('/vault')
        else:
            self.error_text.value = "Invalid username or password. Try again."
            self.error_text.visible = True
            page.update()

