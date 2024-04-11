import flet as fl 
from router import views_handler


def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(views_handler(page)[page.route])


ft.app(target=main)
