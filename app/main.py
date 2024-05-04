import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class MainLayout(BoxLayout):
    pass

    def press_f1(self, instance):
        print("F1")

    def press_f2(self, instance):
        print("F2")

    def search_location(self):
        print(f"{self.search_input.text}")

class MainApp(App):
    def build(self):
        return MainLayout()

def main()-> None:
    MainApp().run()

if __name__ == '__main__':
    main()
