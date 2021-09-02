import os
import cv2
import glob
import time
import shutil
from datetime import date
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from kivy.uix.video import Video
from kivy.core.window import Window
from kivymd.utils.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.imagelist import SmartTileWithLabel
from kivy.properties import StringProperty
Window.size = (360, 640)

kv = """
#: import NoTransition kivy.uix.screenmanager.NoTransition
<ImageTile>:

    MDIconButton:
        icon: "fullscreen"
        theme_text_color: "Custom"
        text_color: (1, 1, 1, 1)
        pos_hint: {"center_x": .9, "center_y": .1}
        on_release:
            app.ImageFullscreen(root.source)
    MDFloatLayout:
        pos_hint: {"center_x": .85, "center_y":.92}
        size_hint: .2, .1
        canvas.before:
            Color:
                rgba: (0, 0, 0, 1)
            RoundedRectangle:
                radius: [20,]
                pos: self.pos
                size: self.size
        MDLabel:
            pos_hint: {"center_x": .5, "center_y": .5}
            text: root.label
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True
            size_hint_x: 1
            halign: "center"

<VideoTile>:

    MDIconButton:
        icon: "play-circle-outline"
        theme_text_color: "Custom"
        text_color: (1, 1, 1, 1)
        user_font_size: "80sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:
            app.VideoFullscreen(root.source)

    MDFloatLayout:
        pos_hint: {"center_x": .85, "center_y":.1}
        size_hint: .2, .1
        canvas.before:
            Color:
                rgba: (0, 0, 0, 1)
            RoundedRectangle:
                radius: [20,]
                pos: self.pos
                size: self.size
        MDLabel:
            pos_hint: {"center_x": .5, "center_y": .5}
            text: root.label
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True
            size_hint_x: 1
            halign: "center"
<Tab@MDFloatLayout+MDTabsBase>

ScreenManager:
    id: sm
    transition: NoTransition()
    
    Screen:
        name: "home"

        MDStackLayout:

            MDToolbar:
                title: "[b]WhatsApp Status Saver[/b]"
                pos_hint: {"top": 1}
                size_hint_y: None
                markup: True
                md_bg_color: .0274509803921569, .3686274509803922, .3294117647058824, 1

            MDTabs:
                on_tab_switch: app.on_tab_switch(*args)
                valign: "center"
                pos_hint_y: None
                indicator_color: (1, 1, 1, 1)
                tab_hint_x: True
                allow_stretch: True
                tab_indicator_height: '5dp'
                background_color: .0274509803921569, .3686274509803922, .3294117647058824, 1
                
                Tab:
                    text: "[b]Images[/b]"
                    markup: True

                    ScrollView:
                        MDGridLayout:
                            id: con
                            adaptive_height: True
                            spacing: 5
                            cols: 2
                            padding: 5
                            md_bg_color: 1, 1, 1, 1       
                Tab:
                    text: "[b]Videos[/b]"
                    markup: True

                    ScrollView:
                        MDGridLayout:
                            id: vcon
                            adaptive_height: True
                            spacing: 5
                            cols: 2
                            padding: 5
                            md_bg_color: 1, 1, 1, 1   

                                
    Screen:
        name: "imgfs"
        
        MDFloatLayout:
            id: imcon
            orientation: "vertical"
            md_bg_color: 0, 0, 0, 1

            MDStackLayout:
                MDToolbar:
                    title: ""
                    pos_hint: {"top": 1}
                    size_hint_y: None
                    markup: True
                    left_action_items: [["arrow-left", lambda x: app.back()]]
                    md_bg_color: .0274509803921569, .3686274509803922, .3294117647058824, 1

                MDCarousel:
                    id: carousel


            MDFloatingActionButton:
                icon: "content-save-outline"
                md_bg_color: .1450980392156863, .8274509803921569, .4, 1 
                pos_hint: {"center_x": .9, "center_y": .1}
                on_release:
                    app.save_image()

    Screen:
        name: "vidfs"
        
        MDFloatLayout:
            id: vicon
            orientation: "vertical"
            md_bg_color: 0, 0, 0, 1
            
            MDStackLayout:
                spacing: 25
                MDToolbar:
                    title: ""
                    pos_hint: {"top": 1}
                    size_hint_y: None
                    markup: True
                    left_action_items: [["arrow-left", lambda x: app.back_from_vid()]]
                    right_action_items: [["content-save", lambda x: app.save_video()]]
                    md_bg_color: .0274509803921569, .3686274509803922, .3294117647058824, 1

                MDFloatLayout:
                    id: vplayercon
                    orientation: "vertical"
                    pos_hint: {"center_x": .5, "center_y":.6}


        MDBoxLayout:
            orientation: "vertical"
            pos_hint: {"center_x": .5, "bottom": 1}
            size_hint_y: .3
            spacing: 10
            margin: 10
            
            canvas.before:
                Color:
                    rgba: 0, 0, 0, .5
                Rectangle:
                    pos: self.pos
                    size: self.size

            MDBoxLayout:
                orientation: "horizontal"
                pos_hint: {"center_x":.5, "center_y":.75}

                MDLabel:
                    id: start
                    text: "0:00"
                    font_size: 14
                    markup: True
                  #  bold: True
                    font_name: "DejaVuSans.ttf"
                    halign: "center"
                    padding: [5,0]
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    pos_hint: {"center_y":.5}
                    size_hint_x: 1

                        
                MDSlider:
                    id:seek
                    min: 0
                    value: 0
                    max: 0
                    hint: False
                    size_hint: 1, None
                    halign: "center"
                    valign: "center"
                    pos_hint: {"center_x":.5, "center_y":.5}
                    color: .9, .3, .3, 1
                    on_active:
                        app.update_seek()
                
                MDLabel:
                    id: end
                    text: "0:00"
                    font_size: 14
                    markup: True
                   # bold: True
                    halign: "center"
                    font_name: "DejaVuSans.ttf"
                    padding: [5,0]
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    pos_hint: {"center_y":.5}
                    size_hint_x: 1
                    


            MDFloatLayout:
                spacing: 50
                padding: 20
                pos_hint: {"center_x": .5}                    

                MDIconButton:
                    icon: "skip-previous"
                    theme_text_color: "Custom"
                    text_color: (1, 1, 1, 1)
                    pos_hint: {"center_x": .25, "center_y":.5} 
                    on_release:
                        app.play_previous(root.ids.vid.source)

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
                        app.playpause()

                MDIconButton:
                    icon: "skip-next"
                    theme_text_color: "Custom"
                    text_color: (1, 1, 1, 1)
                    pos_hint: {"center_x": .75, "center_y":.5} 
                    on_release:
                        app.play_next(root.ids.vid.source)

"""
class ImageTile(SmartTileWithLabel, MDFloatLayout):
    label = StringProperty("")

class VideoTile(SmartTileWithLabel, MDFloatLayout):
    label = StringProperty("")

def generate_thumbnail(video_fn):
    output_fn = video_fn[:-4]+".png"
    vcap = cv2.VideoCapture(video_fn)
    res, im_ar = vcap.read()
    while im_ar.mean() < 50 and res:
          res, im_ar = vcap.read()
    im_ar = cv2.resize(im_ar, (1000, 600), 0, 0, cv2.INTER_LINEAR)
    cv2.imwrite("WSS/Thumbnails/"+output_fn, im_ar)
    return output_fn

class WaSS(MDApp):
    fs_imgs = []
    fs_vids = []
    fs_vid_thumbnails = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(kv)

    def build(self):
        path = "/storage/emulated/0/WhatsApp/Media/.Statuses/*.jpg"
        if not os.path.exists("WSS"): # "storage/emulated/0/WSS"
            os.makedirs("WSS/Images")
            os.makedirs("WSS/Videos")
            os.makedirs("WSS/Thumbnails")
        for i, file in enumerate(glob.glob("*.jpg")):
            self.fs_imgs.append(file)
        for i, file in enumerate(glob.glob("*.mp4")):
            self.fs_vid_thumbnails.append(generate_thumbnail(file))
            self.fs_vids.append(file)
        for i, file in enumerate(self.fs_imgs):
            self.screen.ids.con.rows = i  
            imageTile = ImageTile(
                                        source= file,
                                        size_hint= (1, None),
                                        size= (100, 400),
                                        label=f"{i+1}/{len(self.fs_imgs)}",
                                        )
            self.screen.ids.con.add_widget(imageTile)
        for i, thumbnail in enumerate(self.fs_vid_thumbnails):
            self.screen.ids.vcon.rows = i
            videoTile = VideoTile(
                                        source= thumbnail,
                                        size_hint=(1, None),
                                        size=(100, 400),
                                        label=f"{i+1}/{len(self.fs_vid_thumbnails)}",
                                        )
            self.screen.ids.vcon.add_widget(videoTile)
##        print(self.screen.ids.carousel.current_slide)
        return self.screen

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        return None

    def back(self):
        self.screen.current = "home"
    def back_from_vid(self):
        if self.screen.ids.vid.state == "play":
            self.screen.ids.vid.state = "stop"
        self.screen.current = "home"

    def ImageFullscreen(self, current_source):
        for source in self.fs_imgs:
            ft = FitImage(
                    source=source,
                    pos_hint= {"center_x":.5, "center_y":.5},
                    size_hint= (1, 1))
            self.screen.ids["img"] = ft
            self.screen.ids.carousel.add_widget(ft)
        current_index = self.fs_imgs.index(current_source)
        self.screen.ids.carousel.index = current_index
        self.screen.current = "imgfs"

    def VideoFullscreen(self, current_source):
        self.screen.ids.playpause.icon = "play"
        ft = Video(
                    source=self.fs_vids[self.fs_vids.index(current_source[:-4]+".mp4")],
                    state= "stop",
                    pos_hint= {"center_x": .5, "center_y": .55},
                    options= {"allow_stretch": True},
                    )
        ft.bind(position=self.on_position_change, duration=self.on_duration_change)
        self.screen.ids["vid"] = ft
        self.screen.ids.vplayercon.clear_widgets()
        self.screen.ids.vplayercon.add_widget(ft)
        self.screen.current = "vidfs"



    def on_position_change(self, instance, value):
        # convert to minutes:seconds
        d = self.screen.ids.vid.position
        minutes = int(d / 60)
        seconds = int(d - (minutes * 60))
        # fix label & position
        self.screen.ids.start.text = '%d:%02d' % (minutes, seconds)
        self.screen.ids.seek.value = value

    def on_duration_change(self, instance, value):
        # convert to minutes:seconds
        d = self.screen.ids.vid.duration
        mins = int(d / 60)
        secs = int(d - (mins * 60))
        if secs != 1:
            self.screen.ids.end.text = f"{mins}:{secs}"
        self.screen.ids.seek.min = 0
        self.screen.ids.seek.max = self.screen.ids.vid.duration

    


    def playpause(self):
        self.screen.ids.vid.state = "play" if self.screen.ids.vid.state == "pause" or self.screen.ids.vid.state == "stop" else "pause"
        self.screen.ids.playpause.icon = "pause" if self.screen.ids.vid.state == "play" else "play"

    def update_seek(self):
##        print(self.screen.ids.seek.value)
        self.screen.ids.vid.seek(self.screen.ids.seek.value / self.screen.ids.vid.duration)

    def play_previous(self, current_src):
        current_index = self.fs_vids.index(current_src)
        if current_index == 0:
            return None
        else:
            self.screen.ids.vid.source = self.fs_vids[current_index-1]

    def play_next(self, current_src):
        current_index = self.fs_vids.index(current_src)
        if current_index == len(self.fs_vids)-1:
            return None
        else:
            self.screen.ids.vid.source = self.fs_vids[current_index+1]

    def save_image(self):
        #print(self.screen.ids.carousel.index)
        dnow, c_time = date.today(), time.strftime("%H_%M_%S")
        c_date = dnow.strftime("%m_%d_%y")
        save_as_fn = f"WSS_IMG_{c_date}_{c_time}.png"
        shutil.copy(self.fs_imgs[self.screen.ids.carousel.index], f"WSS/Images/{save_as_fn}")
        toast("Image saved!")

    def save_video(self):
        dnow, c_time = date.today(), time.strftime("%H_%M_%S")
        c_date = dnow.strftime("%m_%d_%y")
        save_as_fn = f"WSS_VID_{c_date}_{c_time}.mp4"
        shutil.copy(self.screen.ids.vid.source, f"WSS/Videos/{save_as_fn}")
        toast("Video saved!")

if __name__ == "__main__":
    WaSS().run()
