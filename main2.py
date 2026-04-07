import flet as ft


def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    greeting_history = []

    history_text = ft.Text(value='История приветствий: ')


    text_hello.value = 'Hello Geeks'
    # text_hello = 'Hello world'


def on_button_click(_):
        print(name_input.value)
        name = name_input.value

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            # text_hello.value = "Hello " + name 

            name_input.value = None

            greeting_history.append(name)
            # print(greeting_history)

            history_text.value = "История приветствий\n" + '\n'.join(greeting_history)
        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите имя'
            print('Ничего не ввели')
        page.update()

    
    name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
    elavated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED, 
                                        icon_color=ft.Colors.GREEN, on_click=on_button_click)

    main_object = ft.Row([name_input, elavated_button])

    page.add(text_hello, main_object, history_text)



ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)

    page.title ='My first app'
    page.theme_mode =ft.ThemeMode.LIGHT
    
    text_hello =ft.Text(value='Hello world')

    text_hello.value ='Hello Geeks'
    text_hello = 'Hello world'

    name






















        
           
