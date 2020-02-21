from datetime import timedelta, datetime
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.uix.label import Label
from kivy.clock import Clock


class NotBdayApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dateNow = datetime.now()
        self.dateEnd = datetime(2020, 4, 24)
        self.difference = self.dateEnd - self.dateNow
        print(self.difference)
        #self.dateNow = datetime.datetime.strftime()

    def build(self):
        time = datetime.today()
        #  Clock.schedule_interval(self.timer, 0.01)
        self.labelTime = Label(text=str(self.difference))
        Clock.schedule_once(self.set_background, 0)
        Clock.schedule_interval(self.timer, 0.01)
        return self.labelTime
        # layout = BoxLayout(padding=10)
        #
        # label1 = Label(text="Hello World", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        # layout.add_widget(label1)
        #
        # label2 = Label(text="Good!", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        # layout.add_widget(label2)
        #
        # button = Button(text="Button")
        # button.bind(on_press=self.on_press_btn)
        # layout.add_widget(button)
        #
        # return layout

    def timer(self, dt):
        self.dateNow = datetime.now()
        self.difference = self.dateEnd - self.dateNow
        #resLine = f"{self.difference.days} дней. {self.difference.}"
        #print(resLine)
        self.labelTime.text = str(self.difference)

    def set_background(self, *args):
        self.root_window.bind(size=self.do_resize)
        with self.root_window.canvas.before:
            self.bg = Rectangle(source="Kate_01.jpg", pos=(0, 0), size=(self.root_window.size))

    def do_resize(self, *args):
        self.bg.size = self.root_window.size

    def on_press_btn(self, instance):
        print("Кнопка нажата")

if __name__ == "__main__":
    NotBdayApp().run()