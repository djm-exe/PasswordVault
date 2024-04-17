import flet as ft
from database import PasswordVault

class VaultScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # def LogOut(vault):
        #     vault = PasswordVault()

        self.content=ft.Column(
            controls=[
                ft.Text('Vault'),
                ft.ElevatedButton(text='Logout')
            ]
        )
