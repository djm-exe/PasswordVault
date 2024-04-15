import flet as ft
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.home import HomeScreen

def views_handler(page):
    return{
        '/': ft.View(
            route='/',
            controls=[HomeScreen(page)],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        '/login': ft.View(
            route='/login', 
            controls=[LoginScreen(page)],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        '/register': ft.View(
            route='/register', 
            controls=[RegisterScreen(page)],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    }
