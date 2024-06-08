from pathlib import Path
from .management_pembimbing_dosen.gui import ManagementPembimbingDosen
from .modul_pembimbing_dosen.gui import ModulPembimbingDosen
#from tkinter import Frame
from tkinter import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainmng():
    MainMNG()

class MainMNG(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        # Set the background color
        self.configure(bg="#313131")

        self.windows = {
            "mng": ManagementPembimbingDosen(self),
            "mdl": ModulPembimbingDosen(self),
        }


        self.current_window = self.windows["mng"]
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