import flet as ft

class RegisterScreen(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.content=ft.Column(
            controls=[
                ft.Text("Register Screen"),
                ft.TextField(label="Username", width=150),
                ft.TextField(label="Password", width=150),
                ft.ElevatedButton(text='Go Back', on_click= lambda _: page.go('/'))
            ]
        )
