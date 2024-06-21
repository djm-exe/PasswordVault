import flet as ft
from database import PasswordVault

class VaultScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        def LogOut(e):
            PasswordVault('master_password').__del__()
            page.go('/')

        self.items_column = ft.Column()

        self.content = ft.Column(
            controls=[
                ft.Text('Vault'),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text='Logout', on_click=LogOut)
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    controls=[
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_item)
                    ]
                ),
                self.items_column  # Add this line
            ],
        )

    def add_item(self, e):
        self.items_column.controls.append(ft.Text('New item'))
        self.update()
