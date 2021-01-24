from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.core.image import Image
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory
from kivy.animation import Animation
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import IRightBodyTouch, IRightBody, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox, MDSwitch
from kivymd.uix.card import MDCardSwipe, MDCard
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout






Window.clearcolor = (1, 0, 1, 1)
Window.keyboard_anim_ards = {"d": .2, "t": "in_out_expo"}
Window.softinput_mode = "below_target"







KV = '''
#: import NoTransition kivy.uix.screenmanager.NoTransition
<CustomToolbar>:
    size_hint_y: None
    height: self.theme_cls.standard_increment
    spacing: "1dp"

##    MDIconButton:
##        id: button_1
##        icon: "menu"
##        pos_hint: {"center_y": .5}
##        on_release: app.menu_1.open()
##        theme_text_color: "Custom"
##        text_color: 1, 1, 1, 1

    MDLabel:
        text: "WhatsApp"
        pos_hint: {"center_y": .5}
        padding: [20, 0]
        size_hint_x: None
        width: self.texture_size[0]
        text_size: None, None
        font_style: 'H6'
        theme_text_color: "Custom"
        specific_text_color: 1, 1, 1, 1
        text_color: 1, 1, 1, 1

    Widget:


    MDIconButton:
        id: button_2
        icon: "magnify"
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







        
ScreenManager:
    id: sm
    transition: NoTransition()
    

    Screen:
        name: "home"

        StackLayout:
        
            CustomToolbar:
                id: toolbar
                pos_hint: {"top": 1}
                md_bg_color: .8941, .4235, .0392, 1


            MDTabs:
                id: tabs
                on_tab_switch: app.on_tab_switch(*args)
                valign: "center"
                pos_hint_y: None
                background_color: .8941, .4235, .0392, 1
                allow_stretch: True
                default_tab: 1
                color_indicator: 1, 1, 1, 1


    ##############################
                Tab:
                    text: "camera"

                    MDFloatLayout:
                        MDSpinner:
                            size_hint: None, None
                            size: dp(40), dp(40)
                            pos_hint: {'center_x': .5, 'center_y': .5}
                            active: True
                            determinate: False
                            color: .8941, .4235, .0392, 1



    ####################################
                Tab:
                    text: "[b]CHATS[/b]"
                    

                
                    BoxLayout:
                        orientation: "vertical"

                        ScrollView:
                        
                            MDList:
                   
                                TwoLineAvatarListItem:
                                    text: "Martin Chinanu"
                                    secondary_text: "Hello bro"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"
           
                                   



        ##                            ImageLeftWidget:
        ##                                source: "data/logo/kivy-icon-256.png"

                                TwoLineAvatarListItem:
                                    text: "Moses"
                                    divider: "Full"
                                    secondary_text: "kjbsdljdbldkjbdlkjdbsklj"
                                    

                                    ImageLeftWidget:
                                        source: "data/logo/kivy-icon-256.png"

                                TwoLineAvatarListItem:
                                    text: "Bro"
                                    secondary_text: "Hello bro"
                                    divider: "Full"

                                    ImageLeftWidget:
                                        source: "data/logo/kivy-icon-256.png"

                                TwoLineAvatarListItem:
                                    text: "Sis"
                                    secondary_text: "Hello bro"
                                    divider: "Full"

                                    ImageLeftWidget:
                                        source: "data/logo/kivy-icon-256.png"

                                TwoLineAvatarListItem:
                                    text: "Mum"
                                    secondary_text: "Hello bro"
                                    divider: "Full"

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                        canvas:
                                            Color:
                                                rgba: .8941176470588235, .8941176470588235, .8941176470588235, 1 
                                            Ellipse:
                                                id: DP
                                                pos: self.pos
                                                size: 38, 38
                                                source: "account.png"

                                TwoLineAvatarListItem:
                                    text: "Dad"
                                    secondary_text: "Hello bro"
                                    divider: "Full"

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                        canvas:
                                            Color:
                                                rgba: .8941176470588235, .8941176470588235, .8941176470588235, 1 
                                            Ellipse:
                                                id: DP
                                                pos: self.pos
                                                size: 38, 38
                                                source: "account.png"




                                TwoLineAvatarListItem:
                                    id: myg
                                    text: "HSSP World Programmers"
                                    secondary_text: "Hello everyone"
                                    divider: "Full"
                                    on_release:
                                        sm.transition.direction = 'left'
                                        sm.current = "gchat"

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Color:
                                                rgba: 1, 1, 1, 1
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"


                                TwoLineAvatarListItem:
                                    text: "Learn247"
                                    secondary_text: "Thanks"
                                    divider: "Full"


                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Color:
                                                rgba: 1, 1, 1, 1
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"














    ######################################
                Tab:
                    text: "[b]STATUS[/b] "

                
                    BoxLayout:
                        orientation: "vertical"


        ##                canvas.before:
        ##                    Color:
        ##                        rgba: 1, 0, 1, 1
        ##                    Rectangle:
        ##                        pos: 0, 200
        ##                        size: 200, 100
        ##


                        ScrollView:
                        
                            MDList:
                   
                                TwoLineAvatarListItem:
                                    text: "My status"
                                    secondary_text: "Tap to add status update"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 40, 40
                                                source: "Martin_3.jpg"       




                                TwoLineAvatarListItem:
                                    text: "My status"
                                    secondary_text: "Tap to add status update"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.05, 0.005
                                        on_touch_down: print("Touched down!")
                                            
                                        canvas:
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 40, 40
                                                source: "Martin_3.jpg"  


                                TwoLineAvatarListItem:
                                    text: "My status"
                                    secondary_text: "Tap to add status update"
                                    divider: "Full"
                                    
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.05, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 40, 40
                                                source: "Martin_3.jpg"  














                    
                                MDFloatingActionButton:
                                    id: status
                                    icon: "pencil"
                                    pos_hint: {"center_x": .9, "center_y": .635}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: 1, .7, .4, 1
                                    user_font_size: "25sp"
                                    on_release: app.file_manager_open()

                                                    
                        
                                MDFloatingActionButton:
                                    id: camera
                                    icon: "camera"
                                    pos_hint: {"center_x": .9, "center_y": .4}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: .9941, .5235, .1392, 1
                                    on_release:
                                        app.takeScreenshot()
                                        toast('Screenshot saved!', duration = 1)


    ####################################
                Tab:
                    text: "[b]CALLS[/b]"

                    BoxLayout:
                        orientation: "vertical"

                        ScrollView:
                        
                            MDList:
                   
                                TwoLineAvatarIconListItem:
                                    text: "Martin Chinanu"
                                    secondary_text: "Today, 2:20 PM"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: DP
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"  
                                    IconRightWidget:
                                        icon: "phone"
                                        theme_text_color: "Custom"
                                        text_color: .8941, .4235, .0392, 1

                                TwoLineAvatarIconListItem:
                                    text: "Sinaayo"
                                    secondary_text: "Today, 2:10 PM"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: DP
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"  
                                    IconRightWidget:
                                        icon: "video"
                                        theme_text_color: "Custom"
                                        text_color: .8941, .4235, .0392, 1




                                TwoLineAvatarIconListItem:
                                    text: "Folasayo Oladeni"
                                    secondary_text: "December 14, 10:37 PM"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: DP
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"  
                                    IconRightWidget:
                                        icon: "video"
                                        theme_text_color: "Custom"
                                        text_color: .8941, .4235, .0392, 1



                                TwoLineAvatarIconListItem:
                                    text: "Bro"
                                    secondary_text: "December 13, 09:05 AM"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"  
                                    IconRightWidget:
                                        icon: "video"
                                        theme_text_color: "Custom"
                                        text_color: .8941, .4235, .0392, 1




                                TwoLineAvatarIconListItem:
                                    text: "Sis"
                                    secondary_text: "December 10, 10:31 AM"
                                    divider: "Full"
                                    

                                    ImageLeftWidget:
                                        size_hint: 0.005, 0.005

                                            
                                        canvas:
                                            Ellipse:
                                                id: 'DP'
                                                pos: self.pos
                                                size: 38, 38
                                                source: "Martin_3.jpg"  

                                    IconRightWidget:
                                        icon: "phone"
                                        theme_text_color: "Custom"
                                        text_color: .8941, .4235, .0392, 1


                                        
                        
                                MDFloatingActionButton:
                                    id: camera
                                    icon: "phone-plus"
                                    pos_hint: {"center_x": .9, "center_y": .4}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    md_bg_color: .9941, .5235, .1392, 1
                                    on_release:
                                        app.show_confirmation_dialog()
                                
    Screen:
        name: "gchat"

        canvas.before:
            Color:
                rgba: 1, 0, 1, .1
            Rectangle:
                pos: self.pos
                size: self.size
                source: "bg-chat-tile-light.png"



        GroupChatToolbar:
            id: groupchat
            pos_hint: {"top": 1}
            md_bg_color: .9941, .5235, .1392, 1
            size_hint_y: None
            height: self.theme_cls.standard_increment
            spacing: "1dp"
            

            canvas:
                Color:
                    rgba: 1, 0, 1, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
                    source: "Martin_3.jpg"
                    on_touch_down: app.animImage(self)
                    
                    
            
##                Image:
##                    source: "Martin_3.jpg"
##                    opacity: .1
##                    pos: self.pos
##                    size: self.size


            MDIconButton:
                icon: "arrow-left"
                pos_hint: {"center_y": .5}
                on_release:
                    sm.current = "home"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
##
##                Widget:
##                
##                    canvas:
##                        Color:
##                            rgba: 1, 1, 1, 1
##                        Ellipse:
##                            id: 'DP'
##                            pos: self.pos
##                            size: 40, 40
##                            source: "Martin_3.jpg"  
##


            MDList:
                pos_hint: {"center_y": .5}
                TwoLineListItem:
                    id: gchatname
                    text: "[b]HSSP World Programmers[/b]"
                    secondary_text: "Abass, Alice, Abass, Blessing, Gift, Martin, Sinaayo "
                    theme_text_color: "Custom"
                    secondary_theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    secondary_text_color: 1, 1, 1, 1
                    secondary_font_style: "Body2"
                    divider: None
                    on_release:
                        sm.current = "gsettings"



            MDIconButton:
                id: addacc
                icon: "phone-plus"
                pos_hint: {"center_y": .5}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                on_release:
                    app.show_example_custom_bottom_sheet()


            MDIconButton:
                id: menu
                icon: "dots-vertical"
                pos_hint: {"center_y": .5}
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                on_release: app.animImage(self)
        MDBoxLayout:
            orientation: "vertical"
            spacing: 20
            padding: 20

            MDCard:
                orientation: "vertical"
                size_hint: None, None
                size: "100dp", "50dp"
                pos_hint: {"center_y": .5, "center_x": .5}

                MDLabel:
                    text: "TODAY"
                    pos: self.pos
                    size_hint_y: None
                    theme_text_color: "Custom"
                    padding: [10, 10]
                    text_color: .8941, .4235, .0392, 1

                    

        BoxLayout:
            spacing: 60
            margin: 10
            padding: 40
            orientation: "horizontal"


            ClickableTextFieldRound:
                id: msgbar
##                size_hint_y: None
##                height: text_field.height
##                size_hint_x: None
                width: "300dp"
                hint_text: "Type a message"
##                pos_hint: {"center_x": .5, "center_y": .5}

                MDTextFieldRound:
                    id: text_field
                    hint_text: msgbar.hint_text
                    text: msgbar.text
                    color_active: 1, 1, 1, 1
                    normal_color: 1, 1, 1, 1
                    size_hint: .3, .1
                    pos_hint: {"bottom": .1, "center_x": .25, "center_y": .005}
                    multiline: True
                    padding:
                        self._lbl_icon_left.texture_size[1] + dp(10) if self.icon_left else dp(15),                 (self.height / 2) - (self.line_height / 2),                 self._lbl_icon_right.texture_size[1] + dp(20),                 0

                MDIconButton:
                    source: "paperclip.png"
                    ripple_scale: .5
                    pos_hint: {"center_y": .5}
                    pos: self.pos
##                    pos: text_field.width - self.width + dp(8), 0
##                    on_release:
##                        self.icon = "eye" if self.icon == "eye-off" else "eye-off"
##                        text_field.password = False if text_field.password is True else True









































##            MDTextFieldRound:
##                hint_text: "Type a message"
##                halign: "center"
##                icon_right: "camera"
##                icon_right_color: .8941, .4235, .0392, 1
##                icon_left: "account"
##                icon_left_color: .8941, .4235, .0392, 1
##                normal_color: 1, 1, 1, 1
##                color_active: 1, 0, 1, 1
##                focus: False
##                size_hint: .3, .1
##                pos_hint: {"bottom": .1, "center_x": .25, "center_y": .005}
##                multiline: True
##                font_size: 20
##                specific_text_color: 1, 1, 1, 1
##                color_mode: 'custom'
##                line_color: 1, 1, 1, 1
##                on_text:
##                    root.ids.micsend.icon = "send" if root.ids.micsend.icon == "microphone" else "send" 
##    ##                root.ids.micsend.icon = "microphone" if root.ids.micsend.icon == "send" else "send"     

            MDFloatingActionButton:
                id: micsend
                icon: "microphone"
                halign: "center"
                size: 50, 50
                pos_hint: {"bottom": .1, "center_y": .005}
                md_bg_color: .8941, .4235, .0392, 1
                text_color: 1, 1, 1, 1




























    Screen:
        name: "card"

        MDCard:
            orientation: "vertical"
            size_hint: .3, .5
            pos_hint: {"center_x": .5, "center_y": .5}


            MDBoxLayout:
                id: container
                orientation: "vertical"
            
            
                FitImage:
                    source: "Martin_3.jpg"
                    size_hint: 1, .9
##                    height: text_box.height
                    pos_hint: {"top": 1}

                MDSeparator:

                MDBoxLayout:
                    id: text_box
                    orientation: "horizontal"
                    adaptive_height: True
                    spacing: "10dp"
                    padding: "10dp", "10dp", "10dp", "10dp"
                            


                    MDIconButton:
                        icon: "message-reply-text"


                    MDIconButton:
                        icon: "phone"


                    MDIconButton:
                        icon: "video"


                    MDIconButton:
                        icon: "help-circle"


    Screen:
        name: "gsettings"
        
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
##                rgba: .8941176470588235, .8941176470588235, .8941176470588235, 1
            Rectangle:
                pos: self.pos
                size: self.size



        MDBoxLayout:
            orientation: "vertical"
            
        
            GroupSettingsToolbar:
                id: groupsettings
                pos_hint: {"top": 1}
                md_bg_color: .9941, .5235, .1392, 1
                size_hint_y: None
                height: self.theme_cls.standard_increment
                spacing: "1dp"


                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_y": .5}
                    on_release:
                        sm.current = "gchat"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1



                MDList:
                    pos_hint: {"center_y": .5}
                    TwoLineListItem:
                        id: gname
                        text: "[b]HSSP World Programmers[/b]"
                        secondary_text: "Created by You, 5/12/20"
                        theme_text_color: "Custom"
                        secondary_theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        secondary_text_color: 1, 1, 1, 1
                        secondary_font_style: "Body2"
                        divider: None
                        
                




                MDIconButton:
                    id: addacc
                    icon: "pencil"
                    pos_hint: {"center_y": .5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release:
                        sm.current = "gname"


                MDIconButton:
                    id: addmem
                    icon: "account-plus"
                    pos_hint: {"center_y": .5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release:
                        sm.current = "gaddparts"
                        

##            MDBoxLayout:
##                orientation: "vertical"
##                
            
            ScrollView:

##                MDBoxLayout:
##                    orientation: "vertical"
##                    spacing: 10
##                    
                
##                
##
##
##                    
##                        MDBoxLayout:
##                            orientation: "vertical"
##                            
##
##                                
                MDCard:
                    orientation: "vertical"
                    padding: dp(4), dp(4)
                    spacing: dp(4)                    

                    MDLabel:
                        text: "Media, links, and docs"

                    ScrollView:
                        do_scroll_y: False
                        do_scroll_x: True
                        bar_width: "9dp"
                        
                        MDGridLayout:
                            cols: 10
                            adaptive_height: True
                            padding: dp(4), dp(4)
                            spacing: dp(4)


                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"                    

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"

                            MyTile:
                                source: "Martin_3.jpg"






























































##                MDList:
##                    id: set1
##                    padding: [10, 0, 0, 50]
##                    
##                    OneLineListItem:
##                        text: "Mute notifications"
##                        on_release:
##                            app.show_confirmation_dialog()
##                        
##                        RightSwitch:
##                            id: mn
##                            pos_hint: {"center_y": .5, "center_x":.9}
##                            size_hint: None, None
##                            thumb_color_down: .9941, .5235, .1392, 1
##                            md_bg_color: 1, .7, .4, 1
##                            on_release:
##                                app.show_confirmation_dialog()
##
##
##
##                    OneLineListItem:
##                        text: "Custom notifications"
##                        on_release:
##                            sm.current = "gnotifications"
##
##                    OneLineListItem:
##                        text: "Media visibility"
##
##                    OneLineListItem:
##                        text: "Group settings"
##                        divider: None
##
##
####                    MDCard:
####                        orientation: "vertical"
####                        size: self.size
####                        pos: self.pos
####                        
####                        
##
##
##                    
##                    TwoLineListItem:
##                        padding: "20dp", "20dp", 0, 0
##                        text: "Disappearing messages"
##                        secondary_text: "Off"
##
##                    ThreeLineListItem:
##                        text: "Encryption"
##                        secondary_text: "Messages and calls are end-to-end encrypted."
##                        tertiary_text: "Tap to learn more"
##
##
##                
##                    OneLineIconListItem:
##                        text: "Add participants"
##
##                        ImageLeftWidget:
##                            size_hint: 0.005, 0.005
##                            
##
##                                
##                            canvas:
##
##                                Color:
##                                    rgba: 1, 0, 1, 1
##                                Ellipse:
##                                    id: DP
##                                    size: 35, 35
##                                    source: "account.png"       
##
##
##                    OneLineIconListItem:
##                        text: "Invite via link"
##
##
##                    TwoLineAvatarListItem:
##                        text: "You"
##                        secondary_text: "The CEO of HSSP World"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Martin Chinanu"
##                        secondary_text: "My Life is a testimony"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Sinaayo"
##                        secondary_text: "Hey there! I am using WhatsApp"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Abass"
##                        secondary_text: "Why buy the cow when the milk is free? Da"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Alice"
##                        secondary_text: "."
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Martin Chinanu"
##                        secondary_text: "My Life is a testimony"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Sinaayo"
##                        secondary_text: "Hey there! I am using WhatsApp"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Abass"
##                        secondary_text: "Why buy the cow when the milk is free? Da"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Alice"
##                        secondary_text: "."
##                        divider: None
##
##
##                    TwoLineAvatarListItem:
##                        text: "Martin Chinanu"
##                        secondary_text: "My Life is a testimony"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Sinaayo"
##                        secondary_text: "Hey there! I am using WhatsApp"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Abass"
##                        secondary_text: "Why buy the cow when the milk is free? Da"
##                        divider: None
##
##                    TwoLineAvatarListItem:
##                        text: "Alice"
##                        secondary_text: "."
##                        divider: None
##
##
##
##
##
##













##                    MDCard:
##                        orientation: "vertical"
##                        size_hint: 1, .2
##
##
##                    
##                        MDBoxLayout:
##                            orientation: "vertical"
##
##
##                            
##                    MDCard:
##                        orientation: "vertical"
##                        size_hint_x: 1
##
##
##
##                    
##                        MDBoxLayout:
##                            orientation: "vertical"
##                            





    Screen:
        name: "gname"

        MDBoxLayout:
            orientation: "vertical"
            
            MDToolbar:
                id: groupnametbar
                pos_hint: {"top": 1}
                title: "Enter new subject"
                type: "top"
                specific_text_color: 1, 1, 1, 1
                md_bg_color: .9941, .5235, .1392, 1
                


            MDTextField:
                id: groupname
                hint_text: "subject..."
                text: "HSSP World Programmers"
                mode: 'line'
                active_line: False
                selected: True
                
                
                color_mode: "custom"
                line_color_focus: .9941, .5235, .1392, 1
                line_color_normal: .9941, .5235, .1392, 1
                pos_hint: {"center_y":.9, "center_x": .5}
                size_hint: .9, None
                line_anim: False
                max_text_length: 24
                icon_right: "emoticon-outline"
                icon_right_color: 0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1 
##                on_text_validate:
##                    gname.text = "[b]{}[/b]".format(groupname.text)
##                    gchatname.text = "[b]{}[/b]".format(groupname.text)
##                    myg.text = groupname.text                    
##                on_focus:
##                    groupname.hint_text = ""

            BoxLayout:
                orientation: "horizontal"

                MDRectangleFlatButton:
                    text: "Cancel"
                    text_color: 0, 0, 0, 1
                    line_color: 0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1
                    pos_hint: {"bottom":.1}
                    size_hint: .5, .1
                    on_release:
                        sm.current = "gsettings"

                MDRectangleFlatButton:
                    text: "OK"
                    text_color: 0, 0, 0, 1
                    line_color: 0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1
                    pos_hint: {"bottom":.1}
                    size_hint: .5, .1
                    on_release:
                        gname.text = "[b]{}[/b]".format(groupname.text)
                        gchatname.text = "[b]{}[/b]".format(groupname.text)
                        myg.text = groupname.text
                        sm.current = "gsettings"
                















                

    Screen:
        name: "gaddparts"

        

        MDBoxLayout:
            orientation: "vertical"
            
        
            GAddMorePartsToolbar:
                id: addparts
                pos_hint: {"top": 1}
                md_bg_color: .9941, .5235, .1392, 1
                size_hint_y: None
                height: self.theme_cls.standard_increment
                spacing: "1dp"


                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_y": .5}
                    on_release:
                        sm.current = "gsettings"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1



                MDLabel:
                    text: "Add participants"
                    pos_hint: {"center_y": .5}
                    font_style: "H6"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1

                    

                MDIconButton:
                    id: morepartsearch
                    icon: "magnify"
                    pos_hint: {"center_y": .5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1


            ScrollView:
            
                MDList:
       
                    TwoLineAvatarListItem:
                        text: "Abass"
                        secondary_text: "Already added to the group"
                        divider: None
                        

                        ImageLeftWidget:
                            size_hint: 0.005, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"       




                    TwoLineAvatarListItem:
                        text: "Alice"
                        secondary_text: "Already added to the group"
                        divider: None
                        

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005
                            on_touch_down: print("Touched down!")
                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  


                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                        

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  


                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  


                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  


                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  





                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  




                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  




                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"          


                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  


                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



                    TwoLineAvatarListItem:
                        text: "Alison"
                        secondary_text: "Hey there! I am using WhatsApp"
                        divider: None
                        
                            

                        ImageLeftWidget:
                            size_hint: 0.05, 0.005

                                
                            canvas:
                                Ellipse:
                                    id: 'DP'
                                    pos: self.pos
                                    size: 40, 40
                                    source: "Martin_3.jpg"  



    Screen:
        name: "gnotifications"

        

        MDBoxLayout:
            orientation: "vertical"
            spacing: "5dp"
            
            
        
            GNotificationsToolbar:
                id: gnotns
                pos_hint: {"top": 1}
                md_bg_color: .9941, .5235, .1392, 1
                size_hint_y: None
                height: self.theme_cls.standard_increment
                spacing: "1dp"


                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_y": .5}
                    on_release:
                        sm.current = "gsettings"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1



                MDLabel:
                    text: "Notifications"
                    pos_hint: {"center_y": .5}
                    font_style: "H6"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    

                    

                MDIconButton:
                    id: resetnotsetts
                    icon: "dots-vertical"
                    pos_hint: {"center_y": .5}
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1



        

            OneLineAvatarIconListItem:
                text: "Use custom notifications"
                divider: None
                

                RightCheckbox:


            MDLabel:
                text: "Message notifications"
                theme_text_color: "Custom"
                text_color: .9941, .5235, .1392, 1
                padding: [17, 100]

            TwoLineListItem:
                text: "Notification tone"
                secondary_text: "Default(Leap)"
                divider: "Full"
                
            TwoLineListItem:
                text: "Vibrate"
                secondary_text: "Default"
                divider: "Full"
                
            TwoLineListItem:
                text: "Popup notification"
                secondary_text: "Not available"
                divider: "Full"
                
            TwoLineListItem:
                text: "Light"
                secondary_text: "White"
                divider: "Full"
                
            ThreeLineAvatarIconListItem:
                text:"Use high priority notifications"
                secondary_text: "Show previews of notifications at the top of"
                tertiary_text: "the screen"
                divider: "Full"

                RightCheckbox:















<MyTile@SmartTile>
    size_hint_y: None
    height: "80dp"
    box_position: 'header'






<GroupContactsCall@BoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height: "500dp"

    


    GContactsCallToolbar:
        id: gcall
        pos_hint: {"top": 1}
        md_bg_color: 1, 1, 1, 1
        size_hint_y: None
        height: self.theme_cls.standard_increment
        spacing: "1dp"
        border_radius: 25
        radius: [25, 25, 0, 0]



        MDLabel:
            text: "Select contacts to call"
            pos_hint: {"center_y": .5}
            font_style: "H6"
            theme_text_color: "Custom"
            text_color: .9941, .5235, .1392, 1
            padding: [20, 0]

            

        MDIconButton:
            id: gcallcontssearch
            icon: "magnify"
            pos_hint: {"center_y": .5}
            theme_text_color: "Custom"
            text_color: .9941, .5235, .1392, 1



    ScrollView:
    
        MDList:

            OneLineAvatarListItem:
                text: "[b]Abass[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Alice[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Alimi Ayomikun[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Blessing[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Hamzah[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Gift[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]God'swork[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Gordon Okoth Agola[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Hamzah[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Hannington[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Iqra[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]James[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Martin Chinanu[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       


            OneLineAvatarListItem:
                text: "[b]Mayowa Smile[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg"       

            OneLineAvatarListItem:
                text: "[b]Mbah Stephane Willy[/b]"
                divider: None
                

                ImageLeftWidget:
                    size_hint: 0.005, 0.005

                        
                    canvas:
                        Ellipse:
                            id: 'DP'
                            pos: self.pos
                            size: 40, 40
                            source: "Martin_3.jpg" 
<ItemConfirm>:
    on_release: root.set_icon(group)

    CheckboxLeftWidget:
        id: group
        group: "check"

<ShowNotns>:
    on_release: root.set_icon(check)


    CheckboxLeftWidget:
        id: check
          




      
<MNContent>:
    orientation: "vertical"
    spacing: "10dp"
    padding: "1dp"
    size_hint_y: None
    height: "250dp"
    

    ItemConfirm:
        text: "8 hours"
        
    ItemConfirm:
        text: "1 week"

    ItemConfirm:
        text: "Always"

    MDSeparator:
        

    ShowNotns:
        text: "Show notifications"



'''


class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color

class Tab(BoxLayout, MDTabsBase):
    pass

class TabHome(BoxLayout, MDTabsBase):
    pass

class RightCheckbox(IRightBody, MDCheckbox):
    '''Custom right checkbox.'''

class RightSwitch(IRightBodyTouch, MDSwitch):
    '''Custom right switch'''

class GroupChatToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color


class GAddMorePartsToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color

class GContactsCallToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color

class GNotificationsToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color
    





class GroupSettingsToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color



class MNContent(BoxLayout):
    pass


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False

class ShowNotns(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False



class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]



















class Test(MDApp):
    dialog = None
    custom_sheet = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.menu_2 = self.create_menu(
            "Button dots", self.screen.ids.toolbar.ids.button_2,
        )

    def create_menu(self, text, instance):
        menu_items = [{"text": text, "divider": None} for i in range(5)]
        menu = MDDropdownMenu(caller=instance, items=menu_items, width_mult=5, position="auto")
        menu.bind(on_release=self.menu_callback)
        return menu

    def menu_callback(self, instance_menu, instance_menu_item):
        instance_menu.dismiss()

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        return None




    

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Mute notifications for...",
                type="custom",
                content_cls=MNContent(),
##                items=[
##                    ItemConfirm(text="8 hours"),
##                    ItemConfirm(text="1 week"),
##                    ItemConfirm(text="Always")
##                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=(.9941, .5235, .1392, 1)
                    ),

                    MDFlatButton(
                        text="OK", text_color=(.9941, .5235, .1392, 1)
                    ),



                ],
            )
        self.dialog.open()




    def show_example_custom_bottom_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.GroupContactsCall())
        self.custom_sheet.open()



    def animate(self, widget, *args):
        anim = Animation(opacity=0.1)
        anim += Animation(opacity=0.2)
        anim += Animation(opacity=0.3)
        anim += Animation(opacity=0.4)
        anim += Animation(opacity=0.5)
        anim += Animation(opacity=0.6)
        anim += Animation(opacity=0.7)
        anim += Animation(opacity=0.8)
        anim += Animation(opacity=0.9)
        anim += Animation(opacity=1)
        anim.start(widget)





    def animImage(self, widget, *args):
        anIm = Animation(size=(255, 255), pos_hint={"center_y":.1}, duration=.1)
        self.screen.ids.groupchat.height = '50dp'
        self.screen.ids.groupchat.height = '100dp'
        self.screen.ids.groupchat.height = '200dp'
        self.screen.ids.groupchat.height = '300dp'
        self.screen.ids.groupchat.height = '400dp'
        anIm.start(widget)



















    def build(self):
        return self.screen


Test().run()
