import flet as ft
from router import views_handler

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route='/',
                controls=[
                    ft.Text(value='Password Vault', size=50),
                    ft.ElevatedButton(text='Register', on_click=lambda _: page.go('/register')),
                    ft.ElevatedButton(text='Login', on_click=lambda _: page.go('/login'))
                ]
            )
        )
        if page.route == '/register':
            page.views.append(
                views_handler(page)[page.route]
            )
        elif page.route == '/login':
            page.views.append(
                views_handler(page)[page.route]
            )

        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    


ft.app(target=main)
