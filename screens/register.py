import flet as ft
from database import PasswordVault

class RegisterScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        def create_vault(vault):
            vault = PasswordVault(password.value)
            vault.reg_user(username.value, password.value)
            page.go('/login')
            

        username = ft.TextField(label="Username", width= 150)
        password = ft.TextField(label="Password", width= 150)
        self.content=ft.Column(
            controls=[
                ft.Text("Register Screen"),
                username,
                password,
                ft.ElevatedButton(text="Create Vault", on_click= create_vault),
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ],
        )
