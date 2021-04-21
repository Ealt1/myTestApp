from kivy.app import App
from kivy.uix.bubble import Bubble
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window


import os
os.environ['KIVY_IMAGE'] = 'pil,sdl2'
import sys


Builder.load_file("debug1rootMin.kv")


class MyScreen(FloatLayout):
    status = StringProperty()
    status = "Status"


class MyApp(App):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)
        #self.devices = com.find_robots()
        self.device = ""
        self.platform = StringProperty()
        if sys.platform == 'darwin':
            self.platform = 'darwin'
        elif sys.platform == 'linux':
            is_android = 'ANDROID_STORAGE' in os.environ
            if (is_android):
                self.platform = 'android'
            else:
                self.platform = 'linux'
        else:
            plaform = 'unsupported'

    def build(self):
        return MyScreen()
        #

if __name__ == '__main__':

    myApp = MyApp()
    myApp.run() 