import flet as ft

def page(page: ft.Page):
    page.title = 'homework'

    count = ft.Text('0')
    def click():
        count.value = str(int(count.value) + 1)

    button = ft.ElevatedButton('Жми', on_click=click)

    page.add(count, button)

ft.app(target=page)