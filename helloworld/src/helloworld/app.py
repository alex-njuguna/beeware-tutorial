"""
My first application
"""
import httpx
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def greeting(name):
    if name:
        if  name == "Brutus":
            return "BeeWare, the IDE of Python"
        else:
            return f"Hello, {name}"
    return "Hello, Stranger"

class HelloWorld(toga.App):
    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your  name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def say_hello(self, widget):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()

        self.main_window.info_dialog(
            greeting(self.name_input.value.title()),
            payload["body"]
        )


def main():
    return HelloWorld()
