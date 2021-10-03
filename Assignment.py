"""
Project: Basic App Assignment
By: Ogunleke Samuel
On: October 2, 2021
"""

#Imports
from math import sin
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.core.window import Window
import requests
from kivymd.toast import toast
import json
Window.size = (340, 620)

#KV
KV = """
ScreenManager:
    id: sm

    Screen:
        name: "login_signup"

        MDFloatLayout:
            orientation: "vertical"
##            md_bg_color: 1.0, 0.9882352941176471, 0.0, 1

            Image:
                source: "Snapchat-Ghost-logo-removebg.png"
                pos_hint: {"center_x":.5, "center_y":.5}
                size_hint: .3, .3
                color: 1, 1, 1, 1


            MDFloatLayout:
                orientation: "horizontal"


                MDFillRoundFlatButton:
                    text: "[b]Log In[/b]"
                    md_bg_color: 1, 1, 1, 1
                    halign: "center"
                    markup: True
                    size_hint: None, None
                    pos_hint: {"center_x":.33, "center_y":.1}
                    text_color: 0.08627450980392157, 0.09803921568627451, 0.10980392156862745, 1
                    on_release:
                        sm.current = "login"
                        
                MDFillRoundFlatButton:
                    text: "[b]Sign Up[/b]"
                    md_bg_color: 0.054901960784313725, 0.6784313725490196, 1.0, 1
                    halign: "center"
                    markup: True
                    text_color: 1, 1, 1, 1
                    pos_hint: {"center_x":.66, "center_y":.1}
                    size_hint: None, None
                    on_release:
                        sm.current = "signup"



    Screen:
        name: "login"

        MDFloatLayout:
            orientation: "vertical"
            md_bg_color: (1, 1, 1, 1)

            MDLabel:
                text: "Log In"
                theme_text_color: "Custom"
                size_hint_x: 1
                halign: "center"
                pos_hint: {"center_x": .5, "center_y": .7}
                font_style: "H4"

            MDSeparator:
                height: 1.5
                size_hint_x: .5
                pos_hint: {"center_x": .5, "center_y": .65}

                
            MDIconButton:
                icon: "chevron-left"
                theme_text_color: "Custom"
                text_color: 0.7254901960784313, 0.7529411764705882, 0.7803921568627451, 1
                pos_hint: {"center_x":.04, "center_y":.94}
                on_release:
                    sm.current = "login_signup"       

            MDFloatLayout:
                size_hint: (.8, .5)
                pos_hint: {"center_x": .5, "center_y": .5}

##                canvas.before:
##                    Color:
##                        rgba: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
##                    RoundedRectangle:
##                        size: self.size
##                        pos: self.pos
####                        source: "pp-sept-blurred.png"
##                        radius: [20,]

                MDTextField:
                    id: email
                    hint_text: "Email"
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    mode: "fill"
                    current_hint_text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    input_type: "mail"
                    size_hint_x: .9
                    pos_hint: {"center_x": .5, "center_y": .63}
                    line_color_normal: (1, 1, 1, 1)
                    line_color_focus: (1, 1, 1, 1)

                MDTextField:
                    id: pwd
                    hint_text: "Password"
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    mode: "fill"
                    current_hint_text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    size_hint_x: .9
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    radius: [0, 0, 10, 10]
                    pos_hint: {"center_x": .5, "center_y": .37}
                    line_color_normal: (1, 1, 1, 1)
                    line_color_focus: (1, 1, 1, 1)
                    password: True

                MDTextButton:
                    text: "Sign Up"
                    pos_hint: {"center_x": .8, "center_y": .2}
                    theme_text_color: "Custom"
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    on_release:
                        sm.current = "signup"

            MDFillRoundFlatButton:
                text: "[b]               Log In               [/b]"
                md_bg_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                halign: "center"
                markup: True
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x":.5, "center_y":.1}
                size_hint: None, None
                disabled: False if pwd.text != "" and email.text != "" else True
                on_release:
                    app.sign_in_existing_user(email.text, pwd.text)



    Screen:
        name: "signup"

        MDFloatLayout:
            orientation: "vertical"
            md_bg_color: (1, 1, 1, 1)

            MDLabel:
                text: "Sign Up"
                theme_text_color: "Custom"
                size_hint_x: 1
                halign: "center"
                pos_hint: {"center_x": .5, "center_y": .85}
                font_style: "H4"

            MDSeparator:
                height: 1.5
                size_hint_x: .5
                pos_hint: {"center_x": .5, "center_y": .8}

                
            MDIconButton:
                icon: "chevron-left"
                theme_text_color: "Custom"
                text_color: 0.7254901960784313, 0.7529411764705882, 0.7803921568627451, 1
                pos_hint: {"center_x":.04, "center_y":.94}
                on_release:
                    sm.current = "login_signup"       

            MDFloatLayout:
                size_hint: (.8, .7)
                pos_hint: {"center_x": .5, "center_y": .5}

##                canvas.before:
##                    Color:
##                        rgba: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
##                    RoundedRectangle:
##                        size: self.size
##                        pos: self.pos
####                        source: "pp-sept-blurred.png"
##                        radius: [20,]
                MDTextField:
                    id: nme
                    hint_text: "Name"
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    mode: "fill"
                    current_hint_text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    size_hint_x: .9
                    pos_hint: {"center_x": .5, "center_y": .75}
                    line_color_normal: (1, 1, 1, 1)
                    line_color_focus: (1, 1, 1, 1)

                MDTextField:
                    id: eml
                    hint_text: "Email"
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    mode: "fill"
                    current_hint_text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    radius: [0,]
                    size_hint_x: .9
                    input_type: "mail"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    line_color_normal: (1, 1, 1, 1)
                    line_color_focus: (1, 1, 1, 1)

                MDTextField:
                    id: pawd
                    hint_text: "Password"
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    mode: "fill"
                    current_hint_text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    size_hint_x: .9
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    radius: [0,]
                    pos_hint: {"center_x": .5, "center_y": .45}
                    line_color_normal: (1, 1, 1, 1)
                    line_color_focus: (1, 1, 1, 1)
                    password: True

                MDTextField:
                    id: cpawd
                    hint_text: "Confirm password"
                    theme_text_color: "Custom"
                    color_mode: "custom"
                    mode: "fill"
                    current_hint_text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    size_hint_x: .9
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    radius: [0, 0, 10, 10]
                    pos_hint: {"center_x": .5, "center_y": .3}
                    line_color_normal: (1, 1, 1, 1)
                    line_color_focus: (1, 1, 1, 1)
                    password: True

                MDTextButton:
                    text: "Log In"
                    pos_hint: {"center_x": .8, "center_y": .2}
                    theme_text_color: "Custom"
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    on_release:
                        sm.current = "login"

            MDFillRoundFlatButton:
                text: "[b]               Sign Up               [/b]"
                md_bg_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                halign: "center"
                markup: True
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x":.5, "center_y":.1}
                disabled: False if nme.text != "" and eml.text != "" and pawd.text != "" and cpawd.text != "" and pawd.text == cpawd.text else True
                on_release:
                    app.sign_up(nme.text, eml.text, pawd.text)
                    
        


    Screen:
        name: "home"

        MDBottomNavigation:
            id: con
            text_color_active: (0, 0, 0, 1)
            text_color_normal: (.7, .7, .7, 1)
            panel_color: (1, 1, 1, 1)

            MDBottomNavigationItem:
                name: "home"
                text: "Home"
                icon: "home-outline"
                on_tab_release:
                    self.icon = "home"
                on_leave:
                    self.icon = "home-outline"

                MDFloatLayout:
                    id: graph_con
                    md_bg_color: (1, 1, 1, 1)

                    MDSeparator:
                        height: 1
                        size_hint_x: 1
                        color: (0, 0, 0, 1)


            MDBottomNavigationItem:
                name: "search"
                text: "Search"
                icon: "magnify"

                MDSeparator:
                    height: 1
                    size_hint_x: 1
                    color: (0, 0, 0, 1)


            MDBottomNavigationItem:
                name: "notifications"
                text: "Notifications"
                icon: "bell-outline"
                on_tab_release:
                    self.icon = "bell"
                on_leave:
                    self.icon = "bell-outline"

                MDSeparator:
                    height: 1
                    size_hint_x: 1
                    color: (0, 0, 0, 1)

            MDBottomNavigationItem:
                name: "profile"
                text: "You"
                icon: "account-circle-outline"
                on_tab_release:
                    self.icon = "account-circle"
                on_leave:
                    self.icon = "account-circle-outline"

                MDSeparator:
                    height: 1
                    size_hint_x: 1
                    color: (0, 0, 0, 1)

                MDTextButton:
                    text: "Sign Out"
                    pos_hint: {"center_x": .8, "center_y": .2}
                    theme_text_color: "Custom"
                    text_color: (0.054901960784313725, 0.6784313725490196, 1.0, 1)
                    on_release:
                        app.sign_out()
"""

#Classes
class AssignmentApp(MDApp):
    web_api_key = "AIzaSyCXQ-EBGVhSK0wCYGEv3FeUqEXsIGvZDOs"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def on_start(self):
        try:
            # Try to read the persistent signin credentials (refresh token)
            with open("refresh.token", "r") as f:
                refresh_token = f.read()
            # Use refresh token to get a new idToken
            id_token, local_id = self.exchange_refresh_token(refresh_token)
            self.local_id = local_id
            self.id_token = id_token
            self.screen.current = "home"
        except Exception as e:
            print(e)

    def build(self):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=6, ymin=0, ymax=4)
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(0,2), (1, 1), (2,1), (4,3), (5,2), (6,4)]
        graph.add_plot(plot)
        self.screen.ids.graph_con.add_widget(graph)
        return self.screen

    def sign_up(self, name, email, password):
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.web_api_key
        payload = {"name": name, "email": email, "password": password, "returnSecureToken": True}
        request = requests.post(url, data=payload)
        data = json.loads(request.content.decode())
        if request.ok == True:
            ref_token = data['refreshToken']
            localId = data['localId']
            idToken = data['idToken']

            with open("refresh.token", "w") as f:
                f.write(ref_token)

            self.local_id = localId
            self.id_token = idToken


        elif request.ok == False:
            error_data = json.loads(request.content.decode())
            error_msg = error_data["error"]['message']
            if error_msg == "EMAIL_EXISTS":
                self.sign_in_existing_user(email, password)
            else:
                toast(error_message.capitalize().replace("_", " "))

    def sign_out(self):
        with open("refresh.token", "w") as s:
            s.write("")
        self.screen.current = "login"

    def sign_in_existing_user(self, email, password):
        url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + self.web_api_key
        payload = {"email": email, "password": password, "returnSecureToken": True}
        request = requests.post(url, data=payload)
        data = json.loads(request.content.decode())

        if request.ok == True:
            ref_token = data['refreshToken']
            localId = data['localId']
            idToken = data['idToken']
            with open("refresh.token", "w") as f:
                f.write(ref_token)

            self.local_id = localId
            self.id_token = idToken
            self.on_start()

        elif request.ok == False:
            error_data = json.loads(request.content.decode())
            error_message = error_data["error"]['message']
            toast("Email exists - "+error_message.replace("_", " "))

    def exchange_refresh_token(self, refresh_token):
        ref_url = "https://securetoken.googleapis.com/v1/token?key=" + self.web_api_key
        ref_payload = '{"grant_type": "refresh_token", "refresh_token": "%s"}' % refresh_token
        ref_req = requests.post(ref_url, data=ref_payload)
        id_token = ref_req.json()['id_token']
        local_id = ref_req.json()['user_id']
        return id_token, local_id            

#Driver code
if __name__ == "__main__":
    AssignmentApp().run()
