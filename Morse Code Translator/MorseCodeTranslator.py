""" Morse Code Translator
By: Ogunleke Samuel Ayomide
On: 21ST MAY, 2021 :: 11:36AM
"""

#Imports
from kivymd.app import MDApp
from kivy.lang import Builder
#0.17647058823529413, 0.1607843137254902, 0.14901960784313725, 1

#KV
KV = """
ScreenManager:
    id: sm

    Screen:
        name: "translator"

        MDFloatLayout:
            orientation: "vertical"
            md_bg_color: 1, 1, 1, 1

            MDLabel:
                text: "Morse-English Translator"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.5, "center_y":.8}
                text_color: 0, 0, 0, 1
                font_style: "H4"

                
            MDBoxLayout:
                orientation: "horizontal"
                size_hint_x: .7
                pos_hint: {"center_x":.5, "center_y":.6}

                MDTextField:
                    id: inp
                    hint_text: "Enter Morse code" if ddi.current_item == "MORSE" else "Enter English word"
                    multiline: True
                    current_hint_text_color: 0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                    text_color: 0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                    line_color_normal: 0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                    line_color_focus: 0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    size_hint: 1, None
                    font_size: 20
                    cursor_color: 0.17647058823529413, 0.1607843137254902, 0.14901960784313725, 1
                    cursor_width: 3
                    selection_color: 0, 0, 0, .2
                    pos_hint: {"center_y": .5}
                    on_text:
                        app.translate()
                        
                    
                MDDropDownItem:
                    id: ddi
                    text: "Select"
                    pos_hint: {"center_y": .5}
                    current_item: "ENGLISH"
                    text_color: 0.17647058823529413, 0.1607843137254902, 0.14901960784313725, 1 
                    on_release:
                        self.set_item("MORSE") if \
                        self.current_item == "ENGLISH" else \
                        self.set_item("ENGLISH")
                    

            MDSeparator:
                width: 2
                size_hint: .7, None
                pos_hint: {"center_x":.5, "center_y":.5}

            MDLabel:
                id: ind
                text: "MORSE" if ddi.current_item == "ENGLISH" else "ENGLISH"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.5, "center_y":.4}
                text_color: 0.9137254901960784, 0.23529411764705882, 0.29411764705882354, 1 # 0.23529411764705882, 0.29411764705882354, 0.9137254901960784, 1
                font_style: "H6"

            MDTextFieldRound:
                id: res
                text: ""
                theme_text_color: "Custom"
                halign: "center"
                line_color: 0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                normal_color: 1, 1, 1, 0
                color_active:  1, 1, 1, 0
                _color_active: 1, 1, 1, 0
                size_hint: .7, None
                pos_hint: {"center_x":.5, "center_y":.3}
                text_color: 0.9137254901960784, 0.29411764705882354, 0.23529411764705882, 1
                font_size: 50
                selection_color: 0, 0, 0, 0.1
                bold: True
                readonly: True
                cursor_color: self.line_color
                cursor_width: 3

            MDLabel:
                text: "Powered by •Horld Translator"
                theme_text_color: "Custom"
                halign: "center"
                size_hint: 1, None
                pos_hint: {"center_x":.5, "bottom": 1}
                text_color: 0.8, 0.8, 0.8, 1
                font_style: "Subtitle2"

            
"""

#Classes

class MCTranslator(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
    def build(self):
        return self.screen

    def translate(self):
        import string
        lettersnnumbers = string.ascii_lowercase
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
           "  ": " "
           } 
        inputText = self.screen.ids.inp.text.lower()
        outputText = ""
        indicator = self.screen.ids.ddi.current_item
        if indicator == "ENGLISH":
            for t in morse.keys():
                if t in inputText.split('  '):
                    nt = morse[t]
                    inputText = inputText.replace(t, nt+" ")
                    outputText = inputText
    ##        print(outputText)
            self.screen.ids.res.text = outputText

        else:
            outputList = []
            for t in inputText.split(' '):
                if t in english.keys():
##                    print(t)
                    nt = english[t]
##                    print(nt)
                    if t == "  ":
                        outputList.append(" ")
                    print(inputText)
                    outputList.append(nt)
                    outputText = ''.join(outputList)
                    print(outputList)
                    print(outputText)
##                    print(nt)
##                    inputText.replace(t, nt)
##                    outputText = inputText
##            print(outputText)
##            self.screen.ids.res.text = outputText


#Driver
if __name__ == "__main__":
    MCTranslator().run()
