# from datetime import date
from datetime import datetime
import random
# pip install flet[all]
import flet as ft 

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    def on_click_button(e):
        name = name_input.value

        now = datetime.now()

        formatted_time = now.strftime("%Y:%m:%d - %H:%M:%S")

        text_hello.value = f"{formatted_time} Hello,{name}!"

        name_input.value = None

    def on_click_random(e):
        name_random = ['Мария', 'Алексей', 'Ольга']
        randomaizer = random.choice(['Мария', 'Алексей', 'Ольга'])
        name_input.value = randomaizer

    name_input = ft.TextField(label='Введите имя', on_submit=on_click_button, expand=True)
    random_button = ft.IconButton(ft.Icons.ADD_ALARM_OUTLINED, on_click=on_click_random)

    main_object = ft.Row([name_input, random_button])

    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    page.add(text_row, main_object)


ft.app(target=main)