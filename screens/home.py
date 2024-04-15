import flet as ft

class HomeScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text('Password Vault', size=50),
                ft.ElevatedButton(text='Register', on_click= lambda _: page.go('/register')),
                ft.ElevatedButton(text='Login', on_click= lambda _:page.go('/login'))
            ]
        )
