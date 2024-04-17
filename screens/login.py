import flet as ft
from database import PasswordVault

class LoginScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()


        username = ft.TextField(label='Username', width= 150)
        password = ft.TextField(label='Password', width= 150)
        self.content=ft.Column(
            controls=[
                ft.Text("Login Screen"),
                username,
                password,
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ]
        )
