from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = """
ScreenManager:
    Screen:
        name: "home"
        MDBoxLayout:
            orientation: "vertical"
            MDTopAppBar:
                title: "Dharam Window Python Edition v3"
                left_action_items: [["window-closed-variant", lambda x: None]]
            MDLabel:
                text: "Dharam Window - Python + KivyMD + SQLite\\n\\nPDF Fix Edition - Save to Downloads"
                halign: "center"
            MDBoxLayout:
                padding: 20
                spacing: 20
                MDRaisedButton:
                    text: "Draw"
                    on_release: app.root.current = "draw"
                MDRaisedButton:
                    text: "Bill"
                    on_release: app.root.current = "bill"
                MDRaisedButton:
                    text: "Cut"
                    on_release: app.root.current = "cut"
    Screen:
        name: "draw"
        MDLabel:
            text: "Draw Screen - Window Elevation\\n(Next step ma banavsu)"
            halign: "center"
    Screen:
        name: "bill"
        MDLabel:
            text: "Bill Screen\\n(Next step ma banavsu)"
            halign: "center"
    Screen:
        name: "cut"
        MDLabel:
            text: "Cutting List Screen\\n(Next step ma banavsu)"
            halign: "center"
"""

class DharamWindowApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

if __name__ == "__main__":
    DharamWindowApp().run()
