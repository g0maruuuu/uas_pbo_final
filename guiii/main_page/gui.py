from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from guiii.main_bimbingan_mahasiswa.main_bimbing import MainBimbing
from guiii.main_bimbingan_mahasiswa.bimbingan_mahasiswa.gui import BimbinganMahasiswa
from guiii.main_bimbingan_mahasiswa.modul_bimbingan_mahasiswa.gui import ModulBimbinganMahasiswa
from guiii.main_logbook.main_lgbk import MainLogbook
from guiii.main_logbook.input_logbook.gui import InputLogbook
from guiii.main_logbook.view_logbook.gui import ViewLogbook

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\main_page\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainpage(user_npm):
    MainPage(user_npm)
#window = Tk()

#window.geometry("1200x700")
#window.configure(bg = "#303030")

class MainPage(Toplevel):
    def __init__(self, user_npm, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.user_npm = user_npm
        self.geometry("1200x700")
        self.current_window = None
        self.configure(bg="#313131")
        self.canvas = Canvas(
            self,
            bg="#303030",
            height=700,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1201.0,
            34.0,
            fill="#7DC3F6",
            outline=""
        )

        self.canvas.create_text(
            4.0,
            0.0,
            anchor="nw",
            text="SimpleLog",
            fill="#000000",
            font=("Helvetica", 22, "bold italic")
        )

        self.canvas.create_rectangle(
            0.0,
            34.0,
            100.0,
            700.0,
            fill="#283948",
            outline=""
        )

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.button_1, "main_bimbg"),
            activebackground="#283948",
            relief="flat"
        )
        self.button_1.place(
            x=5.0,
            y=39.0,
            width=89.0,
            height=78.0
        )

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.button_2, "main_lgbk"),
            activebackground="#283948",
            relief="flat"
        )
        self.button_2.place(
            x=4.0,
            y=129.0,
            width=89.0,
            height=78.0
        )

        button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            activebackground="#283948",
            relief="flat"
        )
        self.button_3.place(
            x=4.0,
            y=597.0,
            width=89.0,
            height=78.0
        )

        # Initialize windows dictionary
        self.windows = {
            "main_bimbg": MainBimbing(self, user_npm),
            "bimbgmh": BimbinganMahasiswa(self, user_npm),
            "mdlsis": ModulBimbinganMahasiswa(self, user_npm),
            "main_lgbk": MainLogbook(self, user_npm),
            "viewlgbk": ViewLogbook(self, user_npm),
            "inptlgbk": InputLogbook(self, user_npm),
        }

        print("Windows initialized:", self.windows)  # Debugging statement

        self.handle_btn_press(self.button_1, "main_bimbg")
        self.current_window.place(x=101, y=34, width=1099.0, height=666.0)
        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()
    
    def handle_btn_press(self, caller, name):
        print(f"Switching to window: {name}")  # Debug statement
        if not hasattr(self, 'windows'):
            print("Error: 'windows' attribute not found")
            return
        if self.current_window:
            self.current_window.place_forget()

        self.current_window = self.windows.get(name)
        if self.current_window:
            self.current_window.place(x=101, y=34, width=1099.0, height=666.0)
        else:
            print(f"Error: Window '{name}' not found in windows dictionary")

        


#window.resizable(False, False)
#window.mainloop()
