import flet as ft
from database import PasswordVault

class VaultScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        def LogOut():
            PasswordVault(master_password=None).__del__()
            page.go('/')

        self.content=ft.Column(
            controls=[
                ft.Text('Vault'),
                ft.ElevatedButton(text='Logout', on_click= LogOut)
            ]
        )
