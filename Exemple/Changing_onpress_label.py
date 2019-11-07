# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random

from kivy.lang import Builder
Builder.load_string("""                 #Pour gérer la partie KV soit on ecrit le contenue directement dans cette methode de cette facon ou alors on renseigne de cette meme facon un fichier local avec ce contenue
                                        #Lorque le language KV est utiliser, il est pas necessaire d'importer quoi que ce soit.
<YourWidget>:
    BoxLayout:
        size: root.size
        Button:
            id: button1
            text: "Change text"
            on_release: root.change_text()
        Label:
            id: label1
            text: root.random_number

""")


class YourWidget(Widget):
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(YourWidget, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(random.randint(1, 100))

class YourApp(App):
    def build(self):
        return YourWidget()

if __name__ == '__main__':
    YourApp().run()
