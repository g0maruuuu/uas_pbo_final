from pathlib import Path
from tkinter import *
from .view_logbook.gui import ViewLogbook
from .input_logbook.gui import InputLogbook
import controller as db_controller
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainlgbk():
    MainLogbook()

class MainLogbook(Frame):
    def __init__(self, parent, user_npm, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_npm = user_npm
        # Set the background color
        self.configure(bg="#313131")

        self.windows = {
            "viewlgbk": ViewLogbook(self,user_npm),
            "inptlgbk": InputLogbook(self),
        }


        self.current_window = self.windows["viewlgbk"]
        self.current_window.place(x=0, y=0, width=1099, height=666)

        self.current_window.tkraise()
        

    def navigate(self, name):
        # Hide all screens
        print(f"Switching to window: {name}")
        #if self.current_window:
            #self.current_window.place_forget()
        for window in self.windows.values():
            window.place_forget()
        self.current_window = self.windows.get(name)
        self.windows[name].place(x=0, y=0, width=1099, height=666)  