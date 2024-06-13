from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, StringVar, Toplevel, Frame
from guiii.pembimbing_main.main_mng import MainMNG
from guiii.pembimbing_main.management_pembimbing_dosen.gui import ManagementPembimbingDosen
from guiii.pembimbing_main.modul_pembimbing_dosen.gui import ModulPembimbingDosen

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def mainPageAdmin(user_nidn):
    MainPageAdmin(user_nidn)

class MainPageAdmin(Toplevel):
    def __init__(self, user_nidn, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.user_nidn = user_nidn
        self.geometry("1200x700")
        self.configure(bg="#313131")
        self.current_window = None
        self.current_window_label = StringVar()
        self.canvas = Canvas(
            self,
            bg="#313131",
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

        button_image_1 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.button_1, "main_mng"),
            activebackground="#283948",
            relief="flat",
        )
        self.button_1.place(
            x=6.0,
            y=39.0,
            width=89.0,
            height=86.0
        )

        button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            activebackground="#283948",
            relief="flat"
        )
        self.button_2.place(
            x=4.0,
            y=597.0,
            width=89.0,
            height=78.0
        )

        self.windows = {
            "main_mng": MainMNG(self, user_nidn),
            "management_pembimbing": ManagementPembimbingDosen(self, user_nidn),
            "mdl": ModulPembimbingDosen(self, user_nidn),
        }

        self.handle_btn_press(self.button_1, "main_mng")
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

    def logout(self):
        self.destroy()
        from guiii.login_page_dosen.gui import LoginDosen
        LoginDosen()
