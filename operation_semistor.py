import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root

try:
    from android.permissions import request_permission, Permission, check_permission

except :
    print('not android')



# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"
else:
    if not check_permission(Permission.RECORD_AUDIO):
        request_permission(Permission.RECORD_AUDIO)
    else:
        print('Permission OK')
    Window.clear()
    Window.borderless = True
    Window.fullscreen = True
    Window.maximize() 


class Operation_semistor(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(Operation_semistor, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "So_Called_Engineers"

        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Dark"

    def build(self):
        return Root()
