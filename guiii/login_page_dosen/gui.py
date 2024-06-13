from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Toplevel, messagebox
from guiii.main_page_admin.gui import mainPageAdmin
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_dosen():
    LoginDosen()

class LoginDosen(Toplevel):
    def loginFunc(self):
        user_nidn = db_controller.checkUserDosen(self.username.get().lower(), self.password.get())
        if user_nidn:
            self.destroy()
            mainPageAdmin(user_nidn)
        else:
            messagebox.showerror(
                title="Invalid Credentials",
                message="The username and password don't match",
            )

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
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            502.0,
            312.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginFunc,
            activebackground="#283948",
            relief="flat"
        )
        button_1.place(
            x=588.0,
            y=480.0,
            width=75.0,
            height=35.0
        )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            503.5,
            395.5,
            image=entry_image_1
        )
        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        self.password.place(
            x=360.0,
            y=363.0,
            width=287.0,
            height=66.0
        )

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            503.5,
            253.5,
            image=entry_image_2
        )
        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        self.username.place(
            x=360.0,
            y=221.0,
            width=287.0,
            height=67.0
        )

        self.username.bind("<Return>", lambda x: self.loginFunc())
        self.password.bind("<Return>", lambda x: self.loginFunc())
        self.resizable(False, False)
        self.mainloop()
