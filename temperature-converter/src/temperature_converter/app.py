"""
Temperature Converter Application with Custom Colors
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER, LEFT, RIGHT


class TemperatureConverter(toga.App):
    def startup(self):
        # Define custom colors
        primary_color = '#3498db'  # Blue
        secondary_color = '#2ecc71'  # Green
        text_color = '#ffffff'  # White

        # Main box containing all elements, aligned to center
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, alignment=CENTER, background_color=primary_color))

        # Box for Fahrenheit input
        f_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=CENTER))
        self.f_input = toga.TextInput(style=Pack(flex=1, padding=(5, 10), background_color=text_color, text_align=CENTER))
        f_label = toga.Label("Fahrenheit", style=Pack(text_align=LEFT, color=text_color))
        f_box.add(f_label)
        f_box.add(self.f_input)

        # Box for Celsius output
        c_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=CENTER))
        self.c_input = toga.TextInput(readonly=True, style=Pack(flex=1, padding=(5, 10), background_color=text_color, text_align=CENTER))
        c_label = toga.Label("Celsius", style=Pack(text_align=RIGHT, color=text_color))
        c_box.add(c_label)
        c_box.add(self.c_input)

        # Label for conversion indication
        join_label = toga.Label("is equivalent to:".title(), style=Pack(text_align=CENTER, padding=10, color=text_color))

        # Button for calculation
        button = toga.Button(
            "Calculate",
            on_press=self.calculate,
            style=Pack(padding=10, flex=1, alignment=CENTER, background_color=secondary_color, color=text_color)
        )

        # Adding all components to the main box
        main_box.add(f_box)
        main_box.add(join_label)
        main_box.add(c_box)
        main_box.add(button)

        # Setting up the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calculate(self, widget):
        """Calculate the conversion from Fahrenheit to Celsius"""
        try:
            fahrenheit = float(self.f_input.value)
            celsius = (fahrenheit - 32.0) * (5 / 9)
            self.c_input.value = f"{celsius:.1f}"
        except ValueError:
            self.c_input.value = "???"


def main():
    return TemperatureConverter()

