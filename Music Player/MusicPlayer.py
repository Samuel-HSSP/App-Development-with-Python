from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from mutagen.mp3 import MP3
from kivy.clock import Clock
import os

Window.size = (320, 640)

from kivy.factory import Factory
##Factory.register('MDCircularLayout', module='kivymd.uix.circularlayout')



# function to convert the seconds into readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds

source = "jaymikee_like-a-tree.mp3"
audio = MP3(source)
au_info = audio.info
len_in_secs = int(au_info.length)
print(len_in_secs)

hours, mins, seconds = convert(len_in_secs)

#print("Hours:", hours)
#print("Minutes:", mins)
#print("Seconds:", seconds)


def searchAudioFiles(search_path):
    result = []

    for root, dirt, files in os.walk(search_path):
        for file in files:
            if file.endswith("mp3"):
                result.append(os.path.join(root, file))
    return result

##print(searchAudioFiles("C:/"))









kv = """
ScreenManager:
    id: sm

    Screen:
        name: "all_music"

        MDFloatLayout:
            orientation: "vertical"
            md_bg_color: 1, 1, 1, 1

            ScrollView:
                MDList:
                    id: allcon
                    
    Screen:
        name: "home"

        MDBoxLayout:
            orientation: "vertical"
                        
            MDFloatLayout:
                orientation: "vertical"
                size_hint: 1, .7
                
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        source: "studyioimg.jpg"

                MDBoxLayout:
                    id: disc
                    pos_hint: {"center_x":.5, "center_y":.7}
                    size_hint: None, None
                    halign: "center"
                    
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1
                            
                        Ellipse:
                            size: 100, 100
                            pos: self.pos
                            source: "studyioimg.jpg"
                        Line:
                            width: 2
                            ellipse: self.x, self.y, 100, 100

                    MDProgressBar:
                        id: progress
                            
                MDLabel:
                    id: title
                    text: ""
                    font_size: 24
                    markup: True
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 1,1,1,1
                    font_name: "DejaVuSans.ttf"
                    pos_hint: {"center_y":.5}
                    size_hint_x: 1
            
            MDFloatLayout:
                orientation: "vertical"
                md_bg_color: 0, 0, 0, .5
                size_hint_y: .25
##                spacing: "10dp"
                pos_hint: {"center_x":.5, "bottom":1}


                MDBoxLayout:
                    orientation: "horizontal"
                    pos_hint: {"center_x":.5, "center_y":.75}

                    MDLabel:
                        id: start
                        text: "00:00"
                        font_size: 14
                        markup: True
                      #  bold: True
                        font_name: "DejaVuSans.ttf"
                        halign: "center"
                        padding: [15,0]
                        theme_text_color: "Custom"
                        text_color: .5, .5, .5, 1
                        pos_hint: {"center_y":.5}
                        size_hint_x: 1
                        
                    MDIconButton:
                        icon: "skip-previous"
                        theme_text_color: "Custom"
                        text_color: .5, .5, .5, 1
                        pos_hint: {"center_y":.5}
                        user_font_size: "35sp"
                        
                            
                    MDFloatingActionButton:
                        id: playpause
                        icon: "play"
                        pos_hint: {"center_y":.5, "center_x":.5}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: .9, .3, .3, 1
                        elevation: 0
                        user_font_size: "30sp"
                        on_release:
##                            app.play_music()
##                            app.on_playing()

                    MDIconButton:
                        icon: "skip-next"
                        pos_hint: {"center_y":.5}
                        theme_text_color: "Custom"
                        text_color: .5, .5, .5, 1
                        user_font_size: "35sp"
                        

                    MDLabel:
                        id: end
                        text: "00:00"
                        font_size: 14
                        markup: True
                       # bold: True
                        halign: "center"
                        font_name: "DejaVuSans.ttf"
                        padding: [15,0]
                        theme_text_color: "Custom"
                        text_color: .5, .5, .5, 1
                        pos_hint: {"center_y":.5}
                        size_hint_x: 1
                        
                                            
                MDBoxLayout:
                    orientation: "horizontal"
                    pos_hint: {"center_y":.3, "center_x":.5}

                    MDIconButton:
                        id: loop
                        icon: "repeat"
                        pos_hint: {"center_y":.5}
                        theme_text_color: "Custom"
                        text_color: .5, .5, .5, 1
                        on_release:
                            self.text_color = [.3, .6, .9, 1] if\
                            self.text_color == [.5, .5, .5, 1] else\
                            [.5, .5, .5, 1]
                            app.loop_music()
                            
                    MDSlider:
                        id: ctrl
                        min: 0
                        value: 0
                       #max: 0
                        hint: False
                        size_hint: .7, None
                        halign: "center"
                        valign: "center"
                        pos_hint: {"center_x":.5, "center_y":.5}
                        color: .9, .3, .3, 1
                        on_active:
                            app.seek_sound()
                            app.start_stop()
                            app.on_seeking()
                            app.done_playing()

                    MDIconButton:
                        icon: "shuffle"
                        pos_hint: {"center_y":.5}
                        theme_text_color: "Custom"
                        text_color: .5, .5, .5, 1
                        on_release:
                            self.text_color = [.3, .6, .9, 1] if\
                            self.text_color == [.5, .5, .5, 1] else\
                            [.5, .5, .5, 1]


"""

class MusicPlayer(MDApp):
    source = "jaymikee_like-a-tree.mp3"
    sound = SoundLoader.load(source)
    sound_started = False
    playing= False
    sound_secs = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(kv)
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen.ids.title.text = self.source.strip(".mp3")

        if self.sound:
            if self.screen.ids.playpause.icon == "play" and self.sound.state == "stop":
                self.screen.ids.playpause.icon = "pause"
                self.sound.play()
                self.screen.ids.ctrl.value += 1

            elif self.screen.ids.playpause.icon == "pause" and self.sound.state == "play":
                self.screen.ids.playpause.icon = "play"
                self.sound.stop()
                
        if self.screen.ids.ctrl.value == 1:
            Clock.schedule_interval(self.update, 0)
            
        if hours != 0:
            self.screen.ids.end.text = f"{hours}:{mins}:{seconds}"
            self.screen.ids.ctrl.max = len_in_secs
        else:
            if mins < 10:
                nmins = "0"+str(mins)
                self.screen.ids.end.text = f"{nmins}:{seconds}"
                self.screen.ids.ctrl.max = len_in_secs
            else:
                self.screen.ids.end.text = f"{mins}:{seconds}"
                self.screen.ids.ctrl.max = len_in_secs

        for file in searchAudioFiles("C:"):
            self.screen.ids.allcon.add_widget(TwoLineListItem(text=file,
                                                              theme_text_color="Custom"))










        return self.screen

##    def play_music(self):
##        if self.sound:
##            if self.screen.ids.playpause.icon == "play" and self.sound.state == "stop":
##                self.screen.ids.playpause.icon = "pause"
##                self.sound.play()
##                self.screen.ids.ctrl.value += 1
##            elif self.screen.ids.playpause.icon == "pause" and self.sound.state == "play":
##                self.screen.ids.playpause.icon = "play"
##                self.sound.stop()

    def loop_music(self):
        if self.sound:
            if self.screen.ids.ctrl.value == len_in_secs:
                self.screen.ids.ctrl.value = 0
            if self.screen.ids.loop.text_color == [.3, .6, .9, 1]:
                self.sound.loop = True
            else:
                self.sound.loop = False
                
    def seek_sound(self):
        if self.sound:
            self.sound.seek(self.screen.ids.ctrl.value)

##    def on_playing(self):
##        if self.screen.ids.ctrl.value == 1:
##            Clock.schedule_interval(self.update, 0)
        """
            If the value of the control is minimum, update the clock
            if it is not the minimum value, update the seconds to be the
            current value of the control slider. 


        """
    def on_seeking(self):
        self.sound_secs = self.screen.ids.ctrl.value
        minutes, seconds = divmod(self.sound_secs, 60)
        self.screen.ids.start.text = (
            '%02d:%02d'%(int(minutes), int(seconds)))

    def update(self, nap):
        if self.sound.state == "play":
            self.sound_secs += nap
            minutes, seconds = divmod(self.sound_secs, 60)
            self.screen.ids.start.text = (
                '%02d:%02d'%(int(minutes), int(seconds)))

    def start_stop(self):
        self.sound_started = not self.sound_started       

    def reset(self):
        if self.sound_started:
            self.sound_started = False
        self.sound_secs = 0

    def update_counter(self, nap):
        if self.sound_started:
            self.sound_secs += nap

    def done_playing(self):
        if self.sound:
            if self.screen.ids.ctrl.value == self.screen.ids.ctrl.max:
                print("Done Playing!")
                self.screen.ids.ctrl.value = self.screen.ids.ctrl.min



MusicPlayer().run()
