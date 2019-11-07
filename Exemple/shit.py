from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime


class MyApp(BoxLayout):
    def count(self, *varargs):
        self.start = datetime.now()
        Clock.schedule_interval(self.on_timeout, 1)

    def on_timeout(self, *args):
        d = datetime.now() - self.start
        self.lbl1.text = datetime.utcfromtimestamp(d.total_seconds()).strftime("%H.%M.%S")

class MainApp(App):        
    def build(self):
        c = MyApp()

        return c
if __name__ == '__main__':
    MainApp().run()  
