"""
Project: Translator
By: Horld Developers
On: Thursday, August 12, 2021 : 6: 
For: Solving the problem of...
"""

#Imports
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
Window.size = (360, 640)
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
##tts = gTTS("Hello from Horld Developers", lang="en")
##tts.save("tts_test.mp3")


KV = """
ScreenManager:
    id: sm

    Screen:
        name: "trans"

        MDFloatLayout:
            orientation: "vertical"
            md_bg_color: (1, 1, 1, 1)

            MDToolbar:
                title: "Translator"
                theme_text_color: "Custom"
                md_bg_color: (0, 0.30980392156862746, 0.5333333333333333, 1)
                pos_hint: {"top": 1}

            MDTextField:
                id: query
                hint_text: "Enter word to translate"
                current_hint_text_color: (0, 0.30980392156862746, 0.5333333333333333, 1)
                text_color: (0, 0, 0, 1) #rgba
                color_mode: "custom"
                multiline: False
                size_hint_x: 0.9
                selection_color: (0, 0, 0, .2)
                cursor_color: self.line_color_normal
                cursor_width: 1.5
                pos_hint: {"center_x": .5, "center_y": .85} 
                line_color_normal: (0.9529411764705882, 0.5725490196078431, 0.12156862745098039, 1)
                line_color_focus: (0.9529411764705882, 0.5725490196078431, 0.12156862745098039, 1)
                on_text:
                    app.detectIt(self.text) if len(self.text) >= 5 else print("Continue typing")
                on_text_validate:
                    app.translateIt(self.text)

            MDIconButton:
                id: sttt
                icon: "microphone"
                theme_text_color: "Custom"
                text_color: (0.9529411764705882, 0.5725490196078431, 0.12156862745098039, 1)
                pos_hint: {"center_x": .9, "center_y": .86}
                on_release:
                    self.icon = "microphone-off" if self.icon == "microphone" else "microphone"
                    app.listenToIt()


            MDRoundFlatButton:
                id: btn
                text: "[b]Select destination language[/b]"
                theme_text_color: "Custom"
                text_color: (0, 0.30980392156862746, 0.5333333333333333, 1)
                line_color: (0, 0.30980392156862746, 0.5333333333333333, 1)
                pos_hint: {"center_x": .5, "center_y": .77}
                markup: True
                line_width: 1.001
                on_release:
                    app.menu.open()

            MDIconButton:
                id: tts
                icon: "text-to-speech"
                theme_text_color: "Custom"
                text_color: (0.9529411764705882, 0.5725490196078431, 0.12156862745098039, 1)
                pos_hint: {"center_x": .1, "center_y": .7}
                disabled: False  if dest.text != "" and src.text != "" and result.text != "" else True
                on_release:
                    self.disabled = True
                    print("Text-to-speech activating")
                    app.speakIt()

            MDFillRoundFlatButton:
                text: "[b]Translate[/b]"
                theme_text_color: "Custom"
                text_color: (1, 1, 1, 1)
                line_color: (0.9529411764705882, 0.5725490196078431, 0.12156862745098039, 1)
                md_bg_color: (0.9529411764705882, 0.5725490196078431, 0.12156862745098039, 1)
                pos_hint: {"center_x": .85, "center_y": .7}
                markup: True
                line_width: 1.001
                on_release:
                    app.translateIt(query.text)
            


            MDFloatLayout:
                size_hint: (.9, .5)
                orientation: "vertical"
                pos_hint: {"center_x": .5, "center_y": .4}

                canvas.before:
                    Color:
                        rgba: (0.7686274509803922, 0.7686274509803922, 0.7686274509803922, 1)
                    Line:
                        rounded_rectangle: self.x, self.y, self.width, self.height, 20

                MDLabel:
                    id: src
                    text: ""
                    theme_text_color: "Custom"
                    text_color: (0, 0.30980392156862746, 0.5333333333333333, 1)
                    pos_hint: {"center_x": .12, "center_y": .93}
                    font_style: "Subtitle1"
                    halign: "center"
                    bold: True
                    size_hint_x: 1
                                        
                MDLabel:
                    id: dest
                    text: ""
                    theme_text_color: "Custom"
                    text_color: (0, 0.30980392156862746, 0.5333333333333333, 1)
                    pos_hint: {"center_x": .88, "center_y": .93}
                    font_style: "Subtitle1"
                    halign: "center"
                    bold: True
                    size_hint_x: 1

                MDLabel:
                    id: result
                    text: ""
                    theme_text_color: "Custom"
                    text_color: (0, 0, 0, 1)
                    pos_hint: {"center_x": .5, "center_y": .8}
                    font_style: "Body1" # H1, H2, H3, H4, H5, H6, Body, Body1, Subtitle, Subtitle1
                    halign: "center"
                    bold: False
                    font_name: "DejaVuSans.ttf"
                    size_hint_x: 1
                                                                                




            MDLabel:
                text: "Horld"
                theme_text_color: "Custom"
                text_color: (0.7686274509803922, 0.7686274509803922, 0.7686274509803922, 1)
                pos_hint: {"center_x": .5, "center_y": .03}
                font_style: "Subtitle1"
                halign: "center"
                bold: True
                size_hint_x: 1
            
"""

#Classes
class HTranslator(MDApp):
    translator = Translator(service_urls=['translate.googleapis.com'])
    all_langs = {"fr": "French",
                        "nl": "Dutch",
                         "la": "Latin",
                         "ko": "Korean",
                         "es": "Spanish",
                         "yo": "Yoruba",
                         "ig": "Igbo",
                         "en": "English",
                         "ha": "Hausa",
                         "ur": "Urdu",
                         "pt": "Portuguese",
                         "de": "German"
                 }
    key = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "text": "French",
                "viewclass": "OneLineListItem",
                "divider": None,
                "md_bg_color": (1, 1, 1, 1),
                "on_release": lambda x="French": self.menu_callback(x),
            },

            {
                "text": "Dutch",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x=f"Dutch": self.menu_callback(x),
            },
            {
                "text": "Latin",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="Latin": self.menu_callback(x),
            },
            {
                "text": "Korean",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="Korean": self.menu_callback(x),
            },
            {
                "text": "Spanish",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="Spanish": self.menu_callback(x),
            }, 
            {
                "text": "Yoruba",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="Yoruba": self.menu_callback(x),
            }, 
            {
                "text": "Igbo",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="Igbo": self.menu_callback(x),
            }, 
            {
                "text": "Hausa",
                "divider": None,
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Hausa": self.menu_callback(x),
            }, 
            {
                "text": "Urdu",
                "divider": None,
                "viewclass": "OneLineListItem",
                "on_release": lambda x="Urdu": self.menu_callback(x),
            },
            {
                "text": "English",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="English": self.menu_callback(x),
            }, 
            {
                "text": "Portuguese",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="Portuguese": self.menu_callback(x),
            }, 
            {
                "text": "German",
                "viewclass": "OneLineListItem",
                "divider": None,
                "on_release": lambda x="German": self.menu_callback(x),
            } 


        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.btn,
            items=menu_items,
            width_mult=4,
            background_color=(1, 1, 1, 1),
            radius=[dp(10)],
            position="bottom"
        )
    def build(self):
        return self.screen


    def menu_callback(self, text_item):
        self.screen.ids.dest.text = text_item
        self.menu.dismiss()

    def detectIt(self, query):
        try:
            detected = self.translator.detect(query)
            print(detected.lang)
            if detected.lang in self.all_langs.keys():
                self.screen.ids.src.text = self.all_langs[detected.lang]
        except:
            print("An error occured, please try again")

    def translateIt(self, query):
        if self.screen.ids.dest.text != "" and self.screen.ids.src.text != "":
            for key in self.all_langs.keys():
                if self.all_langs[key] == self.screen.ids.dest.text:
                    try:
                        self.key[0] = key
                        result = self.translator.translate(query.lower(), dest=key)
                        self.screen.ids.result.text = result.text
                        tts = gTTS(result.text, lang=key)
                        tts.save("tts.mp3")
                    except:
                        print("Error!")
    def speakIt(self):
        if self.screen.ids.dest.text != "" and self.screen.ids.src.text != "" and self.screen.ids.result.text != "":
            sound = SoundLoader.load("tts.mp3")
            if sound:
                sound.play()
                self.screen.ids.tts.disabled = False
            
    def listenToIt(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
##        try:
        while self.screen.ids.stt.icon == "microphone":
            query = r.recognize_google(audio, language = "en")
            self.screen.ids.query.text += query
##        except Exception as e:
##            print("Error!", e)

#Driver code
if __name__ == "__main__":
    HTranslator().run()
