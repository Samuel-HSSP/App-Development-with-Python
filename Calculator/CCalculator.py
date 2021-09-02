"""
A Complex Calculator Application

Libraries and Modules:
    Kivy
    KivyMD
    NumPy
    Maths

Softwares:
    Python's default IDLE
    Figma

Other resources:
    Google | Internet

Time: 12:32 AM
On: Wednesday, 30th June, 2021

# Happy New Month in advance!

"""

#Imports
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Window.size = (360, 640)
Factory.register("CircularRippleBehavior", module="kivymd.uix.behaviors")
    #Maths Modules
from math import log
from math import sin
from math import asin
from math import cos
print(cos(45))
from math import acos
from math import tan
from math import atan
from math import sqrt
from math import degrees
from math import radians
from math import pi
from math import e
from math import factorial

#KV
KV = """
#: import CircularRippleBehavior kivymd.uix.behaviors.CircularRippleBehavior
#: import ButtonBehavior kivy.uix.behaviors.ButtonBehavior
#: import BackgroundColorBehavior kivymd.uix.behaviors.BackgroundColorBehavior
#: import CircularElevationBehavior kivymd.uix.behaviors.CircularElevationBehavior
#: import time time



<KeyButton@CircularRippleBehavior+CircularElevationBehavior+ButtonBehavior+MDLabel+BackgroundColorBehavior>
    size: 50, 50
    font_size: 30
    font_name: "DejaVuSans.ttf"
    markup: True
    elevation: 8

<SKeyButton@CircularRippleBehavior+CircularElevationBehavior+ButtonBehavior+MDLabel+BackgroundColorBehavior>
##    size: 82, 82
    font_size: 20
    bold: True
    elevation: 8

<ACKeyButton@CircularRippleBehavior+ButtonBehavior+MDLabel+BackgroundColorBehavior>
##    size: 82, 82
    font_size: 20
    bold: True

<ClearKeyButton@CircularRippleBehavior+ButtonBehavior+MDLabel+BackgroundColorBehavior>
##    size: 82, 82
    font_size: 20
    bold: True
    ripple_color: 1, 0.75294117647058823529411764705882, 0, .7
    ripple_scale: 1
    ripple_alpha: 1

ScreenManager:
    id: sm

    Screen:
        name: "calc"

        MDFloatLayout:
            id: overallcon
            orientation: "vertical"
            md_bg_color: app.theme_cls.bg_dark # 1, 1, 1, 1

            MDIconButton:
                icon: "dots-vertical"
                theme_text_color: "Custom"
                text_color: .6, .6, .6, 1
                pos_hint: {"top": 1, "right": 1}
                on_release:
            
            MDTextField:
                id: inp
                theme_text_color: "Custom"
                color_mode: "custom"
                text_color: 0, 0, 0, 1
                cursor_color: 0, 0, 1, 1
                cursor_width: 2.5
                font_size: 45
                line_color_normal: 1, 1, 1, 0
                line_color_focus: 1, 1, 1, 0
                line_anim: False
                active_line: False
                pos_hint: {"center_x":.5, "center_y":.75}
                size_hint: 1, None
                padding: 25
                multiline: True
                max_height: 100
                halign: "right"
                selection_color: [0, 0, 0, .2]
                on_text:
                    inp.font_size = 45 if inp.font_size == 30 else 45
                    res.font_size = 30 if res.font_size == 45 else 30
                    app.calculate()


            MDTextField:
                id: res
                text: '0' if inp.text == "" else ''
                theme_text_color: "Custom"
                text_color: .9, .9, .9, 1
                halign: "right"
                selection_color: [0, 0, 0, .2]
                size_hint_x: 1
                padding: 25
                font_name: "DejaVuSans.ttf"
                multiline: False
                readonly: True
                pos_hint: {"center_x":.5, "center_y":.68}
                font_size: 30
                line_color_normal: 1, 1, 1, 0
                line_color_focus: 1, 1, 1, 0
                line_anim: False
                active_line: False

            MDSeparator:
                width: 1
                color: 0.8980392156862745, 0.8980392156862745, 0.8980392156862745, 1
                pos_hint: {"center_x":.5, "center_y": .6}
                size_hint_x: .8

            MDIconButton:
                icon: "arrow-expand-all"
                theme_text_color: "Custom"
                text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                text_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                pos_hint: {"center_x":.2, "center_y": .55}
                on_release:
                    nd_others.set_state("open")

            ACKeyButton:
                id: ac
                text: "AC" if res.text == "0" else "C"
                theme_text_color: "Custom"
                text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                text_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                pos_hint: {"center_x":.5, "center_y": .55}
                halign: "center"
                font_size: 20
                markup: True
                size_hint: None, None
                font_name: "DejaVuSans.ttf"
                md_bg_color: 0, 0, 0, 0
                on_release:
                    inp.text = "" if self.text == "C" else inp.text
##                    clranim.disabled = False if self.text == "C" else True

                
            MDIconButton:
                icon: "backspace-outline"
                theme_text_color: "Custom"
                text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                text_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                pos_hint: {"center_x":.8, "center_y": .55}
                on_release:
                    inp.text = inp.text[:-1]

            ClearKeyButton:
                id: clranim
                text: ""
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 0
                disabled: True # if ac.text == "C" else False
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: None, None
                size: 1000, 1000





            
            MDFloatLayout:
                id: kcon
                orientation: "vertical"
                md_bg_color: 1, 1, 1, 0
                pos_hint: {"center_x": .5, "center_y":.27}
                size_hint: .9, .5

                canvas.before:
                    Color:
##                        rgba: 0, 0, 0, .9
                        rgba: 0.8980392156862745, 0.8980392156862745, 0.8980392156862745, 1
##                        rgba: 0.21176470588235294, 0.27058823529411763, 0.30980392156862746, 1

                    RoundedRectangle:
                        radius: [25]
                        pos: self.pos
                        size: self.size
##                        source: "interior-frame-living-room-with-colorful-white-sofa.jpg"
##                        source: "yellow-business-desk-front-view.jpg"

                MDSeparator:
                    width: 1.5
                    color: 0.8980392156862745, 0.8980392156862745, 0.8980392156862745, 1
                    pos_hint: {"center_x":.78, "center_y": .5}
                    size_hint: None, .8

                        
                MDGridLayout:
                    rows: 4
                    spacing: 5
                    padding: 10
                    pos_hint: {"center_x":.5, "center_y":.5}

                    MDBoxLayout:
                        spacing: 5

                        KeyButton:
                            text: "7"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
                            size: 20, 20
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size


                        KeyButton:
                            text: "8"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text
                                

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                                    
                        KeyButton:
                            text: "9"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size

                   
                        SKeyButton:
                            text: "×"
                            theme_text_color: "Custom"
                            text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                                    


                    MDBoxLayout:
                        spacing: 5
                        
                        KeyButton:
                            text: "4"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size

                        KeyButton:
                            text: "5"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text


                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                                    
                        KeyButton:
                            text: "6"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text


                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                                    
                        SKeyButton:
                            text: "÷"
                            theme_text_color: "Custom"
                            text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                          text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                                    



                    MDBoxLayout:
                        spacing: 5
                        
                        KeyButton:
                            text: "1"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size

                        KeyButton:
                            text: "2"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                        KeyButton:
                            text: "3"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size

                        SKeyButton:
                            text: "+"
                            theme_text_color: "Custom"
                            text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                          text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                            on_release:
                                inp.text += self.text

                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size
                                    

                    MDBoxLayout:
                        spacing: 5
                        
                        KeyButton:
                            text: "0"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += self.text


                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size

                        KeyButton:
                            text: "•"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 1.0, 0.3411764705882353, 0.2, 1
                            on_release:
                                inp.text += "."

                            canvas.before:
                                Color:
                                    rgba: 1, 0.75294117647058823529411764705882, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size




                        KeyButton:
                            text: "="
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 0.21176470588235294, 0.27058823529411763, 0.30980392156862746, 1
                            on_release:
                                inp.font_size = 30 if inp.font_size == 45 else 30
                                res.font_size = 45 if res.font_size == 30 else 45
                                app.calculate()

                            canvas.before:
                                Color:
                                    rgba: 1, 0.75294117647058823529411764705882, 0, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size

                        SKeyButton:
                            text: "−"
                            theme_text_color: "Custom"
                            text_color: 1, 0.75294117647058823529411764705882, 0, .7
##                          text_color: 1, 1, 1, 1
                            pos_hint: {"center_x":.5, "center_y":.5}
                            halign: "center"
    ##                        md_bg_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                            on_release:
                                inp.text += "-"

                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, .7
                                Ellipse:
                                    pos: self.pos
                                    size: self.size                                

                MDNavigationLayout:
                    MDNavigationDrawer:
                        id: nd_others
##                        radius: [25]
                        border_radius: 10, 0, 0, 0
                        size_hint: None, 1
                        anchor: "right"
                        elevation: 10
                        pos_hint: {"center_y":.541}
                        md_bg_color: 0, 0, 0, .5
##                        md_bg_color: 0.45098039215686275, 0.5764705882352941, 0.7019607843137254, 1
                        open_progress: 0.1

                        MDGridLayout:
                            rows: 5
##                            cols: 3
                            spacing: 5
                            padding: 10
                            pos_hint: {"center_x":.5, "center_y":.5}

                            MDBoxLayout:
                                KeyButton:
                                    text: "INV"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: [0, 0, 0, 0]
                                    on_release:
                                        self.md_bg_color = [0, 0, 0, 1] if self.md_bg_color == [0, 0, 0, 0] else [0, 0, 0, 0]
                                        sin.text = "sin[sup]-1[/sup]" if sin.text == "sin" else "sin"
                                        cos.text = "cos[sup]-1[/sup]" if cos.text == "cos" else "cos"
                                        tan.text = "tan[sup]-1[/sup]" if tan.text == "tan" else "tan"
                                        ln.text = "e[sup]x[/sup]" if ln.text == "In" else "In"
                                        

                                KeyButton:
                                    text: "DEG"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        self.text = "RAD" if\
                                        self.text == "DEG" else\
                                        "DEG"

                                KeyButton:
                                    text: "%"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:

                                KeyButton:
                                    text: "[sup]m[/sup]P[sub]n[/sub]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:

                                KeyButton:
                                    text: "[sup]m[/sup]C[sub]n[/sub]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:

                            MDBoxLayout:      
                                KeyButton:
                                    id: sin
                                    text: "sin"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    markup: True
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += "sin("
                                    

                                KeyButton:
                                    id: cos
                                    text: "cos"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += "cos("


                                KeyButton:
                                    id: tan
                                    text: "tan"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += "tan("


                                KeyButton:
                                    text: "x[sup]2[/sup]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    font_name: "DejaVuSans.ttf"
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:

                                KeyButton:
                                    text: "[sup]3[/sup]√x"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:




                            MDBoxLayout:
                                KeyButton:
                                    id: ln
                                    text: "In"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:



                                KeyButton:
                                    text: "log"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += "log("



                                KeyButton:
                                    text: "√"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += self.text

                                KeyButton:
                                    text: "[sup]y[/sup]√x"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:

                                KeyButton:
                                    text: "x[sup]y[/sup]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    font_name: "DejaVuSans.ttf"
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:




                            MDBoxLayout:
                                KeyButton:
                                    text: "pi"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:


                                KeyButton:
                                    text: "e"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:



                                KeyButton:
                                    text: "^"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    font_size: 20
                                    halign: "center"
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += self.text


                                KeyButton:
                                    text: "±"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:

                                KeyButton:
                                    text: "x[sup]3[/sup]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    font_name: "DejaVuSans.ttf"
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:





                            MDBoxLayout:
                                KeyButton:
                                    text: "("
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += self.text

                                KeyButton:
                                    text: ")"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text += self.text


                                KeyButton:
                                    text: "!"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:
                                        inp.text = "0" if inp.text == "" else inp.text
                                        inp.text += self.text


                                KeyButton:
                                    text: "x[sup]-1[/sup]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    font_name: "DejaVuSans.ttf"
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:


                                KeyButton:
                                    text: "10[sup]x[/sup]"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_x":.5, "center_y":.5}
                                    halign: "center"
                                    font_size: 20
                                    markup: True
                                    font_name: "DejaVuSans.ttf"
                                    md_bg_color: 0, 0, 0, 0
                                    on_release:


                                
"""


#Classes

class Calculator(MDApp):
    reset = False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return self.screen

    def calculate(self):
        # The Usual Calculation
        inp_query = self.screen.ids.inp.text
        background_query = inp_query
        
        operands = ("*", "+", "-", "/")
        if "×" in background_query:
            background_query = background_query.replace("×", "*")
        if "÷" in background_query:
            background_query = background_query.replace("÷", "/")
        if "^" in background_query:
            background_query = background_query.replace("^", "**")

        try:
##            if any(n in background_query for n in operands):
            if background_query.endswith(operands):
                print("None")
                print("We have an operand at the end")

            elif "!" in background_query:
                background_query = f"factorial({background_query.strip('!')})"
                ev = eval(background_query)
                print(background_query)
##                if background_query.endswith(operands):
##                    background_query.replace(background_query, str(ev))
##                    print(background_query)
                print(ev)
                self.screen.ids.res.text = "= "+str(ev)
                
            else:
                simple_eval1 = eval(background_query)
                if any(n in background_query for n in operands):
                    self.screen.ids.res.text = "= "+str(simple_eval1)
                print(simple_eval1)
        except Exception as e:
            print(f"e == {e}")
            print("Bad expression")



#Driver Code
if __name__ == "__main__":
    Calculator().run()
