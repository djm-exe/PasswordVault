import flet as ft

class LoginScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.content=ft.Text("Login")

