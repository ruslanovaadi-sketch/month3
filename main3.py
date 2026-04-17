import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Привет"

    name_input = ft.TextField(label="Введите имя")
    result_text = ft.Text()

    def greet(e):
        now = datetime.now()
        formatted_time = now.strftime("%Y:%m:%d - %H:%M:%S")
        result_text.value = f"{formatted_time} - Привет, {name_input.value}!"
        page.update()

    btn = ft.ElevatedButton(text="Поздороваться", on_click=greet)

    page.add(name_input, btn, result_text)

ft.app(target=main)

        
    