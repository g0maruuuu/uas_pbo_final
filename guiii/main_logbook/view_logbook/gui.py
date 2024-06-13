

from pathlib import Path
from tkPDFViewer import tkPDFViewer as pdf
import chardet
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Toplevel
from tkinter.ttk import Treeview
import controller as db_controller


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def viewlgbk():
    ViewLogbook()
#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#303030")

class ViewLogbook(Frame):
    def __init__(self, parent, user_npm, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_npm = user_npm
        self.configure(bg="#313131")
        self.canvas = Canvas(
            self,
            bg ="#313131",
            height = 666,
            width = 1099,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            15.0,
            47.0,
            990.0,
            539.0,
            fill="#D9D9D9",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("inptlgbk"),
            activebackground="#313131",
            relief="flat"
        )
        button_1.place(
            x=401.0,
            y=560.0,
            width=203.0,
            height=57.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_1 = self.canvas.create_image(
            502.0,
            27.0,
            image=self.image_image_1
        )
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_refresh,
            activebackground="#313131",
            relief="raised"
        )
        button_2.place(
            x=948.0,
            y=5.0,
            width=42.0,
            height=42.0
        )       



        self.columns = {
            "id": ["id", 75],
            "nama": ["nama", 75],
            "npm": ["npm", 75],
            "tanggal": ["tanggal", 75],
            "nama_dosen": ["nama_dosen", 75],
            "tugas": ["tugas", 75],
            "tujuan": ["tujuan", 75],
            "permasalahan_skripsi": ["permasalahan_skripsi", 75],
            "solusi": ["solusi", 75],
            "tugas_minggu_depan": ["tugas_minggu_depan", 75],
            "progress_skripsi": ["progress_skripsi", 75],
            "status_validasi": ["status_validasi", 75],
            "tanggal_submit": ["tanggal_submit", 90],
        }

        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        # Show the headings
        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0])
            # Set the column widths
            self.treeview.column(idx, width=txt[1])

        self.treeview.place(x=15.0, y=47.0, width=990.0, height=492.0)

        self.handle_refresh()
        self.treeview.bind("<ButtonRelease-1>", self.on_treeview_click)

    def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        self.room_data = db_controller.view_logbook(self.user_npm)

        for row in self.room_data:
            if isinstance(row[10], bytes):
                detected_encoding = self.detect_encoding(row[10])
                if detected_encoding:
                    try:
                        row = list(row)
                        row[10] = row[10].decode(detected_encoding)
                    except UnicodeDecodeError as e:
                        # Log the decoding error
                        logging.error(f"Error decoding BLOB data: {e}")
                        row = list(row)  # Convert to list to modify
                        row[10] = "Decoding Error"
                        row = tuple(row)  # Convert back to tuple
                else:
                    row = list(row)  # Convert to list to modify
                    row[10] = "Unknown Encoding"
                    row = tuple(row)  # Convert back to tuple
            self.treeview.insert("", "end", values=row)


    def detect_encoding(self, blob_data):
        result = chardet.detect(blob_data)
        return result['encoding']        

    def on_treeview_click(self, event):
        selected_item = self.treeview.selection()
        if not selected_item:
            return

        item = self.treeview.item(selected_item)
        values = item['values']

        # Assuming 'progress_skripsi' is the 10th column (index 9)
        progress_skripsi = values[10]

        # Open the PDF file if progress_skripsi contains the path or filename
        if progress_skripsi:
            self.open_pdf(progress_skripsi)


    def open_pdf(self, pdf_path):
        pdf_window = Toplevel(self)
        pdf_window.title("PDF Viewer")
        pdf_window.geometry("800x600")

         
        pdf_viewer = pdf.ShowPdf()
        pdf_display = pdf_viewer.pdf_view(pdf_window, pdf_location=pdf_path, width=100, height=100)
        pdf_display.pack(expand=True, fill='both')      
        
