from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox, StringVar
import controller as db_controller
from tkPDFViewer import tkPDFViewer as pdf

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\pembimbing_main\modul_pembimbing_dosen\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def modulpembimbingdosen():
    ModulPembimbingDosen()


class ModulPembimbingDosen(Frame):
    def __init__(self, parent, user_nidn, npm="", id_bimbingan_mahasiswa="", file_skripsi="", *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_nidn = user_nidn
        self.npm = npm
        self.id_bimbingan_mahasiswa = id_bimbingan_mahasiswa
        self.status_validasi = None  # Initialize status_validasi
        self.file_skripsi = file_skripsi
        self.data = {
            "nidn": StringVar(),
            "npm": StringVar(value=npm),
            "id_bimbingan_mahasiswa": StringVar(value=id_bimbingan_mahasiswa),
            "tanggal": StringVar(),
            "konsultasi_pembimbing": StringVar()
        }
        self.configure(bg="#313131")
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

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_1 = self.canvas.create_image(
            502.0,
            19.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            366.5,
            465.5,
            image=self.entry_image_1
        )
        entry_1 = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_1.place(
            x=56.0,
            y=398.0,
            width=621.0,
            height=139.0
        )
        entry_1.insert(tk.END, self.data["konsultasi_pembimbing"].get())
        entry_1.bind("<<Modified>>", lambda event: self.update_tujuan(event, "konsultasi_pembimbing"))

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.save,
            relief="flat"
        )
        button_1.place(
            x=457.0,
            y=554.0,
            width=92.0,
            height=57.0
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_5.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_status("approved"),
            activebackground="#313131",
            relief="flat"
        )
        button_2.place(
            x=33.0,
            y=305.0,
            width=94.0,
            height=60.0
        )

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_4.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("mng"),
            activebackground="#313131",
            relief="flat"
        )
        button_3.place(
            x=0.0,
            y=1.0,
            width=45.0,
            height=36.0
        )
        self.canvas.create_rectangle(
            40.0,
            44.0,
            966.0,
            300.0,
            fill="#D9D9D9",
            outline=""
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            127.0,
            376.0,
            image=self.image_image_2
        )

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_6.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_status("rejected"),
            activebackground="#313131",
            relief="flat"
        )
        button_4.place(
            x=138.0,
            y=305.0,
            width=94.0,
            height=60.0
        )

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_7.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_status("pending"),
            activebackground="#313131",
            relief="flat"
        )
        button_5.place(
            x=243.0,
            y=305.0,
            width=94.0,
            height=60.0
        )

        self.hdr_tanggal = PhotoImage(
            file=relative_to_assets("image_5.png"))
        bg_hdr_tanggal= self.canvas.create_image(
            793.0,
            376.0,
            image=self.hdr_tanggal
        )

        self.img_tanggal = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            809.5,
            417.5,
            image=self.img_tanggal
        )
        entry_tanggal = Entry(
            self,
            textvariable=self.data["tanggal"],
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_tanggal.place(
            x=722.0,
            y=394.0,
            width=175.0,
            height=43.0
        )



        
        self.hdr_nidn = PhotoImage(
            file=relative_to_assets("image_6.png"))
        bg_hdr_tanggal= self.canvas.create_image(
            793.0,
            459.0,
            image=self.hdr_nidn
        )

        self.img_nidn = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            809.5,
            500.5,
            image=self.img_nidn
        )
        entry_nidn = Entry(
            self,
            textvariable=self.data["nidn"],
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_nidn.place(
            x=722.0,
            y=477.0,
            width=175.0,
            height=43.0
        )
        if self.file_skripsi:
            self.open_pdf(self.file_skripsi)
        

    def set_status(self, status):
        self.status_validasi = status

    def update_tujuan(self, event, key):
        widget = event.widget
        self.data[key].set(widget.get("1.0", tk.END).strip())
        widget.edit_modified(False)    

    def save(self):
        # Check if any fields are empty
        for key, val in self.data.items():
            if not val.get():
                messagebox.showinfo("Error", "Please fill in all the fields")
                return

        # Save the data
        result = db_controller.add_bimbingan_dosen(
            self.data["nidn"].get(),
            self.data["npm"].get(),
            self.data["id_bimbingan_mahasiswa"].get(),
            self.data["tanggal"].get(),
            self.data["konsultasi_pembimbing"].get(),
            self.status_validasi
        )

        if result:
            messagebox.showinfo("Success", "Bimbingan sudah diajukan")
            self.parent.navigate("mng")
            self.parent.windows.get("mng").handle_refresh_mng()
            for label in self.data.keys():
                self.data[label].set("")
        else:
            messagebox.showerror("Error", "Unable to add logbook. Please ensure the data is valid.")


    def open_pdf(self, pdf_path):
        
        self.canvas.delete("pdf_viewer")
        # Create a new PDF viewer instance
        pdf_viewer = pdf.ShowPdf()
        
        # Integrate the PDF viewer within the existing canvas
        pdf_display = pdf_viewer.pdf_view(
            self.canvas,
            pdf_location=pdf_path,
            width=200,
            height=200,
        )
        
        # Place the PDF viewer on the canvas
        self.canvas.create_window(
            502, 172,  # Centering the PDF viewer on the canvas
            window=pdf_display,
            tags="pdf_viewer",
            height=256,
            width=926
        )         
