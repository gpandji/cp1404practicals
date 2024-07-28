from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        names = ["Alice", "Bob", "Charlie", "Diana"]
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
