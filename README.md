# Kivy Border Button

This is a simple Kivy project to customise the button draw routine to make a rounded corner button.

## Designing button image

You will need a PNG image with a transparent background and an image that represents the corners of your button. You can use any art package to create this.

## Create your code file

Use an editor to create a `main.py` file. You can copy the following template code into this file:

~~~
from kivy.app import App
from kivy.uix.widget import Widget

class BorderButtonScreen(Widget):
    pass

class BorderButtonApp(App):
    def build(self):
        return BorderButtonScreen()

if __name__ == '__main__':
    BorderButtonApp().run()

~~~

## Create your layout file

Use an editor to create a `borderbutton.kv` file. You can copy the following template layout into this file:
~~~
#:kivy 1.9.0
#:import utils kivy.utils

<BorderButtonScreen>:
    Widget:
        Button:
            text: "MY BUTTON"
            background_color: utils.get_color_from_hex('#0000ff')
            background_normal: 'circle_up.png'
            background_down: 'circle_down.png'
            border: 0, 32, 0, 32
            size: 200, 64
            center: root.width / 2, root.height / 2
~~~

## Test your custom button

You can test by running the following command from the Anaconda prompt:
~~~
python main.py
~~~
