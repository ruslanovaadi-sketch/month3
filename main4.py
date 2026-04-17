import flet as ft
import random

def main(page: ft.Page):
    page.title = "Случайное имя"

    names = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Анна"]

    name_input = ft.TextField(label="Введите имя")

    def random_name(e):
        name_input.value = random.choice(names)
        page.update()

    random_button = ft.ElevatedButton(
        text="Случайное имя",
        on_click=random_name
    )

    page.add(name_input, random_button)

ft.app(target=main)

    



     