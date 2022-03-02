from kivymd.uix.screen import MDScreen


class HomeScreen(MDScreen):

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def start_listing(self,btn):
        print("its working HomeScreen")
    pass
    """
    Example Screen.
    """
