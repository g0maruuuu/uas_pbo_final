from pathlib import Path
from .management_pembimbing_dosen.gui import ManagementPembimbingDosen
from .modul_pembimbing_dosen.gui import ModulPembimbingDosen
#from tkinter import Frame
from tkinter import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainmng():
    MainMNG()

class MainMNG(Frame):
    def __init__(self, parent, user_nidn, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_nidn = user_nidn
        # Set the background color
        self.configure(bg="#313131")

        self.windows = {
            "mng": ManagementPembimbingDosen(self, user_nidn),
            "mdl": ModulPembimbingDosen(self, user_nidn),
        }


        self.current_window = self.windows["mng"]
        self.current_window.place(x=0, y=0, width=1099, height=666)

        self.current_window.tkraise()
        

    def navigate(self, name):
        print(f"Switching to window: {name}")
        for window in self.windows.values():
            window.place_forget()
        self.current_window = self.windows.get(name)
        if self.current_window:
            self.current_window.place(x=0, y=0, width=1099, height=666)
            self.current_window.tkraise() 

    def show_modul_pembimbing_dosen(self, user_nidn, npm, id_bimbingan_mahasiswa, file_skripsi):
        # Create and place ModulPembimbingDosen window with the passed data
        modul_pembimbing_dosen = ModulPembimbingDosen(self, user_nidn, npm, id_bimbingan_mahasiswa, file_skripsi)
        modul_pembimbing_dosen.place(x=0, y=0, width=1099, height=666)
        modul_pembimbing_dosen.tkraise()
        self.current_window = modul_pembimbing_dosen 
