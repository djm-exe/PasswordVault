import flet as ft

class LoginScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.content=ft.Column(
            controls=[
                ft.Text("Login Screen"),
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ]
        )