import flet as ft 
from datetime import datetime

print("Hello")

def main(page: ft.Page):
    page.title = "Моё первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []

    def update_history_view():
        history_controls = [ft.Text("История приветствий:", size="bodyMedium")]
        for idx, name in enumerate(greeting_history):
            history_controls.append(
                ft.Row([
                    ft.Text(name), 
                    ft.IconButton(icon=ft.icons.CLOSE, tooltip="Удалить", on_click=lambda e, i=idx: remove_name_from_history(i))
                ])
            )
        history_column.controls = history_controls
        page.update()

    def remove_name_from_history(index):
        if 0 <= index < len(greeting_history):
            del greeting_history[index]
            update_history_view()

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            hour = datetime.now().hour
            if 6 <= hour < 12:
                greeting = "Доброе утро"
            elif 12 <= hour < 18:
                greeting = "Добрый день"
            elif 18 <= hour < 24:
                greeting = "Добрый вечер"
            else:
                greeting = "Доброй ночи"

            greeting_text.value = f'{greeting}, {name}!'
            name_input.value = ''
            greet_button.text = 'Поздороваться снова'

            greeting_history.append(name)
            update_history_view()
        else:
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

    def clear_history(_):
        greeting_history.clear()
        update_history_view()
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def copy_greeting(_):
        page.set_clipboard(greeting_text.value)

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_7, tooltip="Сменить тему", on_click=toggle_theme)

    name_input = ft.TextField(label="Введите имя", autofocus=True, on_submit=on_button_click)

    greet_button = ft.ElevatedButton("Поздороваться", icon=ft.icons.API, on_click=on_button_click)

    clear_button = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить историю", on_click=clear_history)

    copy_button = ft.IconButton(icon=ft.icons.COPY, tooltip='Скопировать приветствие!', on_click=copy_greeting)

    history_column = ft.Column([])
    update_history_view()

    page.add(
        ft.Row([name_input, theme_button, clear_button, greet_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([greeting_text, copy_button], alignment=ft.MainAxisAlignment.START), 
        history_column
    )

ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER)
