import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")
    greeting_history = []

    def get_greeting_by_time(name: str) -> str:
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

    def update_history_view():
        history_controls = [ft.Text("История приветствий:", size="bodyMedium")]
        for idx, entry in enumerate(greeting_history):
            history_controls.append(
                ft.Row([
                    ft.Text(entry),
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
            greeting = get_greeting_by_time(name)
            greeting_text.value = greeting
            name_input.value = ''
            greet_button.text = 'Поздороваться снова'

            timestamp = datetime.now().strftime("%Y-%m-%d — %H:%M:%S")
            greeting_history.append(f"{timestamp}: {name}")
            update_history_view()
        else:
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

    def clear_history(_):
        greeting_history.clear()
        update_history_view()
        page.update()

    def toggle_theme(_):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def copy_greeting(_):
        page.set_clipboard(greeting_text.value)

    # UI элементы
    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_7, tooltip="Сменить тему", on_click=toggle_theme)
    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)
    greet_button = ft.ElevatedButton("Поздороваться", icon=ft.icons.API, on_click=on_button_click)
    clear_button = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить историю", on_click=clear_history)
    copy_button = ft.IconButton(icon=ft.icons.COPY, tooltip="Скопировать приветствие", on_click=copy_greeting)

    history_column = ft.Column()
    update_history_view()

    # Разметка
    page.add(
        ft.Row([theme_button, clear_button], alignment=ft.MainAxisAlignment.END),
        greeting_text,
        name_input,
        greet_button,
        copy_button,
        history_column
    )

ft.app(target=main)
