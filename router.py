import flet as ft
from screens.login import LoginScreen
from screens.register import RegisterScreen

def view_handler(page):
    return{
        '/login': ft.View(route='/login', controls=[LoginScreen(page)]),
        '/register': ft.View(route='/register', controls=[RegisterScreen(page)])
    }