from pathlib import Path
from tkinter import *
from .modul_bimbingan_mahasiswa.gui import ModulBimbinganMahasiswa
from .bimbingan_mahasiswa.gui import BimbinganMahasiswa
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainbimbing():
    MainBimbing()

class MainBimbing(Frame):
    def __init__(self, parent, user_npm, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_npm = user_npm
        # Set the background color
        self.configure(bg="#313131")

        self.windows = {
            "mdlsis": ModulBimbinganMahasiswa(self, user_npm),
            "bimb": BimbinganMahasiswa(self, user_npm),
        }


        self.current_window = self.windows["bimb"]
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