from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# class GridLayoutExample(GridLayout):
#     pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3=Button(text="C")
    #     self.orientation='vertical'
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class AnchorLayoutExample(AnchorLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
