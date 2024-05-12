from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
import os
import re

class DataInput(TextInput):
    pattern = re.compile('[^0-9a-fA-F]')
    def insert_text(self, substring, from_undo=False):
        pattern = self.pattern
        filtered_text = re.sub(pattern, '', substring)
        if len(self.text) % 3 == 2 and filtered_text != "":
            filtered_text = ' ' + filtered_text
        if len(self.text) >= 11:
            filtered_text = ""
        return super().insert_text(filtered_text, from_undo=from_undo)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    console_text = ObjectProperty(None)
    send_data = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.console_text.text = stream.read()

        self.dismiss_popup()

    def can_send(self):
        print(f"Send Data: {self.send_data.text}")
        self.console_text.text += f"Received: {self.send_data.text}\n"

class MainApp(App):
    pass

Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('Root', cls=Root)

def main() -> None:
    MainApp().run()

if __name__ == '__main__':
    main()

