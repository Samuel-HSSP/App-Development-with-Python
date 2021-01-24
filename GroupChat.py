from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
Window.clearcolor = (1, 0, 1, 1)
Window.keyboard_anim_ards = {"d": .2, "t": "in_out_expo"}
Window.softinput_mode = "below_target"








KV = '''
<CustomToolbar>:
    size_hint_y: None
    height: self.theme_cls.standard_increment
    padding: "5dp"
    spacing: "12dp"

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .5}
        on_release: app.menu_2.open()
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

    Widget:

        canvas:
        
            Color:
                rgba: 1, 1, 1, 1
            Ellipse:
                id: 'DP'
                pos: self.pos
                size: 30, 30
                source: "Martin_3.jpg"  



##    MDFlatButton:
##        text: "[b]HSSP World Programmers[/b]"
##        pos_hint: {"center_y": .5, "center_x": .1}
##        size: self.size
##        text_color: 1, 1, 1, 1

    MDLabel:
        text: "HSSP World Programmers"
        pos_hint: {"center_y": .5, "center_x": .1}
        padding: [20, 0]
        size_hint_x: None
        width: self.texture_size[0]
        text_size: None, None
        font_style: 'H6'
        theme_text_color: "Custom"
        specific_text_color: 1, 1, 1, 1
        text_color: 1, 1, 1, 1


    MDIconButton:
        id: button_1
        icon: "phone-plus"
        pos_hint: {"center_y": .5}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1


    MDIconButton:
        id: button_2
        icon: "dots-vertical"
        pos_hint: {"center_y": .5}
        on_release: app.menu_2.open()
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1





Screen:

    canvas.before:
        Color:
            rgba: 1, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
            source: "bg-chat-tile-light.png"

    CustomToolbar:
        id: toolbar
        elevation: 10
        pos_hint: {"top": 1}
        md_bg_color: .8941, .4235, .0392, 1


    BoxLayout:
        spacing: 60
        margin: 10
        padding: 40
        orientation: "horizontal"

        MDTextFieldRound:
            hint_text: "Type a message"
            halign: "center"
            icon_right: "camera"
            icon_right_color: .8941, .4235, .0392, 1
            icon_left: "account"
            icon_left_color: .8941, .4235, .0392, 1
            normal_color: [1, 1, 1, 1]
            color_active: [1, 1, 1, 1]
            size_hint: .3, .1
            pos_hint: {"bottom": .1, "center_x": .25, "center_y": .005}
            multiline: False
            font_size: 20
            specific_text_color: 1, 1, 1, 1
            color_mode: 'custom'
            line_color_normal: 1, 1, 1, 1
            line_color_focus: 1, 1, 1, 1
            line_anim: False
            fill_color: 1, 1, 1, 1
            on_text:
                root.ids.micsend.icon = "send" if root.ids.micsend.icon == "microphone" else "send" 
##                root.ids.micsend.icon = "microphone" if root.ids.micsend.icon == "send" else "send"     

        MDFloatingActionButton:
            id: micsend
            icon: "microphone"
            halign: "center"
            size: 50, 50
            pos_hint: {"bottom": .1, "center_y": .005}
            md_bg_color: .8941, .4235, .0392, 1
            text_color: 1, 1, 1, 1

'''


class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.menu_1 = self.create_menu(
            "Button menu", self.screen.ids.toolbar.ids.button_1,
        )
        self.menu_2 = self.create_menu(
            "Button dots", self.screen.ids.toolbar.ids.button_2,
        )

    def create_menu(self, text, instance):
        menu_items = [{"text": text} for i in range(5)]
        menu = MDDropdownMenu(caller=instance, items=menu_items, width_mult=5)
        menu.bind(on_release=self.menu_callback)
        return menu

    def menu_callback(self, instance_menu, instance_menu_item):
        instance_menu.dismiss()

    def build(self):
        return self.screen


Test().run()
