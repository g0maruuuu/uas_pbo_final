


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
#from ..main_page.gui import mainpage
#from ..main_page_admin.gui import mainPageAdmin
from guiii.login_page.gui  import Login
from guiii.login_page_dosen.gui import LoginDosen
import controller as db_controller
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#313131")

def landingpage():
    LandingPage()

class LandingPage(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.geometry("1005x623")
        self.configure(bg = "#313131")
        
        self.canvas = Canvas(
            self,
            bg = "#313131",
            height = 623,
            width = 1005,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_1 = self.canvas.create_image(
            502.0,
            312.0,
            image=image_image_1
        )

        lgn_mahasiswa_image_1 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.login_mahasiswa = Button(
            self.canvas,
            image=lgn_mahasiswa_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.navigasi(self.login_mahasiswa, "lgn_mhs"),
            activebackground="#283948",
            relief="flat"
        )
        self.login_mahasiswa.place(
            x=378.0,
            y=192.0,
            width=243.0,
            height=35.0
        )
        
        lgn_dosen_image_1 = PhotoImage(file=relative_to_assets("button_3.png"))
        login_dosen = Button(
            self.canvas,
            image=lgn_dosen_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.navigasi(self.login_mahasiswa, "lgn_dsn"),
            activebackground="#283948",
            relief="flat"
        )
        login_dosen.place(
            x=378.0,
            y=386.0,
            width=243.0,
            height=35.0
        )
        self.resizable(False, False)
        self.mainloop()

    def navigasi(self, caller, name):
        print(f"Switching to window: {name}")
        self.destroy()  # Close the current window
        if name == "lgn_mhs":
            Login()
        elif name == "lgn_dsn":
            LoginDosen()
        

        

#window.resizable(False, False)
#window.mainloop()
