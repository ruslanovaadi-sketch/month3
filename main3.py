import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Homework3"

    name_input = ft.TextField(label="Введите имя")

    result_text = ft.Text(value="")
    
def show_message(e):
    name = name.input_value

    now = datetime.now()

    formatted_time = now.strftime("%Y:%m:%d - %H:%M:%S")

    result_text.value = f"{formatted_time} Hello,{name}!"
    page.update()

button = ft.ElevatedButton(text="Show",on_click=show_message)

page.add(
    name_input,
    button,
    result_text
)
ft.app(target=main)

        
    