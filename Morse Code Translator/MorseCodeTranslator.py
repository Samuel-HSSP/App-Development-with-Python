""" Morse Code Translator
By: Ogunleke Samuel Ayomide
On: 21ST MAY, 2021 :: 11:36AM
"""

#Imports
from kivymd.app import MDApp
from kivy.lang import Builder
from gtts import gTTS
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
Window.size = (340, 620)

#0.17647058823529413, 0.1607843137254902, 0.14901960784313725, 1
##text = "S a m u e l  A y o m i d e"
##text = text.replace(" ", ".")
##print(text.replace("..", "3"))





#KV
KV = """
ScreenManager:
    id: sm

    Screen:
        name: "translator"

        MDFloatLayout:
            orientation: "vertical"
            md_bg_color: 1, 1, 1, 1

            MDToolbar:
                title: "Morse-English Translator"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                elevation: 5
                pos_hint: {"center_x":.5, "top":1}
##                md_bg_color: 

                
            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, .3
                pos_hint: {"center_x":.5}
                md_bg_color: (1, 1, 1, 1)

            MDLabel:
                text: "Translate your English words to Morse Code and vice versa"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.5, "center_y":.83}
                text_color: app.theme_cls.primary_color
                font_style: "H6"



            MDBoxLayout:
                orientation: "vertical"
                size_hint: 1, .7
                pos_hint: {"center_x":.5}
                md_bg_color: app.theme_cls.primary_color           
          
            MDCard:
                id: cd
                orientation: "vertical"
                size_hint: .95, None
                pos_hint: {"center_x": .5, "center_y":.7}
                elevation: 10
                md_bg_color: (1, 1, 1, 1)
                radius: [10,]

                MDFloatLayout:                
                    FitImage:
                        source: "pp-sept-blurred.png"
                        size_hint: 1, 1
                        pos_hint: {"center_x": .5, "center_y":.5}
                        radius: [10, 10, 10, 10]

                    MDTextField:
                        id: inp
                        hint_text: "Enter Morse code" if ddi.current_item == "Morse" else "Enter English word"
                        multiline: False
                        current_hint_text_color: (1, 1, 1, 1) #0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                        text_color: (1, 1, 1, 1)
                        line_color_normal: (1, 1, 1, 1)
                        line_color_focus: (1, 1, 1, 1)
                        theme_text_color: "Custom"
                        color_mode: "custom"
                        size_hint: .9, None
                        font_size: 20
                        cursor_color: 0.17647058823529413, 0.1607843137254902, 0.14901960784313725, 1
                        cursor_width: 3
                        selection_color: 0, 0, 0, .2
                        pos_hint: {"center_y": .5, "center_x":.5}

                    MDDropDownItem:
                        id: ddi
                        text: "Select"
                        pos: cd.pos
##                        pos_hint: {"center_y": .2, "center_x":.15}
                        current_item: "English"
                        theme_text_color: "Custom"
                        text_color: [1, 1, 1, 1]
                        on_release:
                            self.set_item("Morse") if \
                            self.current_item == "English" else \
                            self.set_item("English")

                        canvas.before:
                            Color:
                                rgba: app.theme_cls.primary_color
                            RoundedRectangle:
                                size: self.size
                                pos: self.pos
                                radius: [0, 20, 0, 10]
                                            
            MDRoundFlatButton:
                text: "[b]       Translate       [/b]"
                theme_text_color: "Custom"
                text_color: (1, 1, 1, 1)
                font_style: "Subtitle1"
                line_color: (1, 1, 1, 1)
                disabled: True if inp.text == "" else False
                line_width: 1.1
                pos_hint: {"center_x":.5, "center_y":.55}
                on_release:
                    app.translate()
                                

            MDSeparator:
                width: 2
                size_hint: .7, None
                color: (.99, .99, .99, 1)
                pos_hint: {"center_x":.5, "center_y":.5}

            MDLabel:
                id: ind
                text: "MORSE" if ddi.current_item == "English" else "ENGLISH"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.5, "center_y":.46}
                text_color: (1, 1, 1, 1) #0.23529411764705882, 0.29411764705882354, 0.9137254901960784, 1
                font_style: "H6"

            MDIconButton:
                icon: "text-to-speech"
                theme_text_color: "Custom"
                text_color: (1, 1, 1, 1)
                pos_hint: {"center_x": .1, "center_y": .44}
                on_release:
                    app.speak()
                    app.update_current()

            MDLabel:
                id: playing
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.9, "center_y":.44}
                text_color: (1, 1, 1, 1)
                font_style: "H6"

            MDBoxLayout:
                size_hint: .9, .35
                pos_hint: {"center_x":.5, "center_y":.2}

                canvas.before:
                    Color:
                        rgba: (1, 1, 1, 1)
                    Line:
                        width: 1.1
                        rounded_rectangle: self.x, self.y, self.width, self.height, 10

                ScrollView:
                    
                    MDTextField:
                        id: res
                        text: ""
                        theme_text_color: "Custom"
                        halign: "center"
                        padding: 10
                        line_color: (0, 0, 0, 0) #0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                        normal_color: 1, 1, 1, 0
                        color_active:  1, 1, 1, 0
                        _color_active: 1, 1, 1, 0
                        size_hint: 1, None
                        pos_hint: {"center_x":.5, "center_y":.5}
                        text_color: (1, 1, 1, 1)
                        font_size: 25
                        selection_color: 0, 0, 0, 0.1
                        multiline: True
                        readonly: True

            
            MDLabel:
                text: "Powered by •Horld Translator"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.5, "bottom": 1}
                text_color: 0.99, 0.99, 0.99, 1
                font_style: "Subtitle2"

            
"""

#Classes

class MCTranslator(MDApp):
    
    playing_currently = ["Nil"]        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen

    def translate2Eng(self, inputText):
        english = {
           ".-": "a",
           "-...": "b",
           "-.-.": "c",
           "-..": "d",
           ".": "e",
           "..-.": "f",
           "--.": "g",
           "....": "h",
           "..": "i",
           ".---": "j",
           "-.-": "k",
           ".-..": "l",
           "--": "m",
           "-.": "n",
           "---": "o",
           ".--.": "p",
           "--.-": "q",
           ".-.": "r",
           "...": "s",
           "-": "t",
           "..-": "u",
           "...-": "v",
           ".--": "w",
           "-..-": "x",
           "-.--": "y",
           "--..": "z",
           ".----": "1",
           "..---": "2",
           "...--": "3",
           "....-": "4",
           ".....": "5",
           "-....": "6",
           "--...": "7",
           "---..": "8",
           "----.": "9",
           "-----": "0",
           "..--..": "?",
           "--..--": ",",
           ".--.-.": "@",
           "-..-.": "/",
           }
##        print(inputText)
        if any(mc in inputText for mc in english.keys()):
##            print("We still have some problems here")
            inputText = inputText.split(' ')
            for t in english.keys():
                if t in inputText:
                    nt = english[t]
                    inputText[inputText.index(t)] = nt
                    return self.translate2Eng(' '.join(inputText))      
        else:
            return inputText

    def translate(self):
        morse = {
           "a": ".-",
           "b": "-...",
           "c": "-.-.",
           "d": "-..",
           "e": ".",
           "f": "..-.",
           "g": "--.",
           "h": "....",
           "i": "..",
           "j": ".---",
           "k": "-.-",
           "l": ".-..",
           "m": "--",
           "n": "-.",
           "o": "---",
           "p": ".--.",
           "q": "--.-",
           "r": ".-.",
           "s": "...",
           "t": "-",
           "u": "..-",
           "v": "...-",
           "w": ".--",
           "x": "-..-",
           "y": "-.--",
           "z": "--..",
           "1": ".----",
           "2": "..---",
           "3": "...--",
           "4": "....-",
           "5": ".....",
           "6": "-....",
           "7": "--...",
           "8": "---..",
           "9": "----.",
           "0": "-----",
           "?": "..--..",
           ",": "--..--",
           "@": ".--.-.",
           "/": "-..-."
           }

        inputText = self.screen.ids.inp.text.lower()
        outputText = ""
        indicator = self.screen.ids.ddi.current_item
        if indicator == "English": # to Morse
            for t in morse.keys():
                if t in inputText:
                    nt = morse[t]
                    inputText = inputText.replace(t, nt+" ")
                    outputText = inputText
            self.screen.ids.res.text = outputText

        else: # to English
            try:
                res = self.translate2Eng(inputText)
                res = res.replace(" ", ".")
                res = res.replace("..", " ")
                res = res.replace(".", "")
                self.screen.ids.res.text = res
            except:
                print("An error occured! Don't try again with the same input")


            try:
                tts = gTTS(self.screen.ids.res.text, lang="en-us")
                tts.save("tts.mp3")
            except:
                print("Error!")


    def speak(self):
        if self.screen.ids.ddi.current_item == "English":
            import glob
            morseCodeAlpha = {}
            import string
            letters = string.ascii_uppercase
            for idx, file in enumerate(glob.glob("Morse-Code-Alphabets/*.mp3")):
                morseCodeAlpha[letters[idx]] = file
            test = self.screen.ids.inp.text.upper()
            import time
            for t in test:
                if t in morseCodeAlpha.keys():
                    try:
                        sound = SoundLoader.load(morseCodeAlpha[t])
                        if sound:
                            self.playing_currently.append(t)
    ##                        print("Fine!")
                            sound.play()
                            time.sleep(2)
                            sound.stop()
                    except:
                         print("Error!")
            print("Okay")
        else:
            print("Translation is from Morse to English")
            sound = SoundLoader.load("tts.mp3")
            if sound:
                sound.play()

    def update_current(self):
        self.screen.ids.playing.text = self.playing_currently[-1]



#Driver
if __name__ == "__main__":
    MCTranslator().run()
