"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMilesToKmApp(App):
    """ Kivy App for converting miles to kilometers """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        """ handle conversion of miles to kilometers """
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * 1.60934
            self.root.ids.output_label.text = str(kilometers)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

    def handle_increment(self, increment):
        """ handle increment and decrement of miles input """
        try:
            miles = float(self.root.ids.input_miles.text)
            miles += increment
            self.root.ids.input_miles.text = str(miles)
        except ValueError:
            self.root.ids.input_miles.text = "0"
            self.root.ids.output_label.text = "Invalid input"


ConvertMilesToKmApp().run()
