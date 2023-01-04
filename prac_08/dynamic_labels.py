from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.label()
        return self.root

    def label(self):
        for name in self.name_to_phone:
            temp_button = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_button)


DynamicWidgetsApp().run()
