from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem

Builder.load_string(
    '''
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>:

    IconLeftWidget:
        icon: root.icon

<PreviousMDIcons>:

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'
                
            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: root.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)

class CustomOneLineIconListItem(TwoLineIconListItem):
    icon = StringProperty()

class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "secondary_text": "Hello there!",
                    "callback": lambda x: x,
                    "divider": None
                }
            )
            
        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
##                    f"[color=#AAAAAA]{name_icon}[/color]"
##                    add_icon_item(f"[color=#AAAAAA]{name_icon}[/color]")
                    add_icon_item(name_icon)
                else:
                    None
            else:
                add_icon_item(name_icon)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen
    
    def on_start(self):
        self.screen.set_list_md_icons()

MainApp().run()















