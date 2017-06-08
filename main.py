from kivy.app import App
from kivy.uix.widget import Widget

class BorderButtonScreen(Widget):
    pass

class BorderButtonApp(App):
    def build(self):
        return BorderButtonScreen()

if __name__ == '__main__':
    BorderButtonApp().run()
