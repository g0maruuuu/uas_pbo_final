from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from tkPDFViewer import tkPDFViewer as pdf
from tkinter.ttk import Treeview
import controller as db_controller
import chardet
#from guiii.pembimbing_main.modul_pembimbing_dosen.gui import ModulPembimbingDosen
#from guiii.pembimbing_main.main_mng import MainMNG
#from guiii.management_pembimbing_dosen.main_mng import navigate


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\pembimbing_main\management_pembimbing_dosen\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#def nav():
    #MainMNG


#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#313131")
def managementpembimbingdosen():
    ManagementPembimbingDosen()


class ManagementPembimbingDosen(Frame):
    def __init__(self, parent, user_nidn, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.user_nidn = user_nidn
        self.configure(bg="#313131")
        self.canvas = Canvas(
            self,
            bg = "#313131",
            height = 666,
            width = 1099,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self._image_image_1 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_1 = self.canvas.create_image(
            549.0,
            160.0,
            image=self._image_image_1
        )

        self._image_image_2 = PhotoImage(file=relative_to_assets("Image_3.png"))
        image_2 = self.canvas.create_image(
            212.0,
            14.0,
            image=self._image_image_2
        )

        self._image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            187.0,
            312.0,
            image=self._image_image_4
        )

        self._image_image_3 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_3 = self.canvas.create_image(
            549.0,
            458.0,
            image=self._image_image_3
        )

        self._button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self._button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.navigate_to_modul,
            activebackground="#313131",
            relief="flat"
        )
        button_1.place(
            x=448.0,
            y=602.0,
            width=203.0,
            height=57.0
        )
        self._button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self._button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_refresh_mng,
            activebackground="#313131",
            relief="raised"
        )
        button_2.place(
            x=1050.0,
            y=5.0,
            width=42.0,
            height=42.0
        )       


        self._columns = {
            "id": ["id", 120],
            "nidn": ["nidn", 120],
            "npm": ["npm", 120],
            "nama_mahasiswa": ["nama_mahasiswa", 120],
            "id_bimbingan_mahasiswa": ["id_bimbingan_mahasiswa", 120],
            "tanggal": ["tanggal", 120],
            "konsultasi_pembimbing": ["konsultasi_pembimbing", 120],
            "status_validasi": ["status_validasi", 135],

        }
        self._treeview = Treeview(
            self,
            columns=list(self._columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        for idx, txt in self._columns.items():
            self._treeview.heading(idx, text=txt[0])
            # Set the column widths
            self._treeview.column(idx, width=txt[1])

        self._treeview.place(x=62.0, y=29.0, width=975.0, height=262.5)
        self.handle_refresh_mng()
        #self.treeview.bind("<ButtonRelease-1>", self.on_treeview_click)

        self._columns_2 = {
            "id": ["id", 139],
            "npm": ["npm", 139],
            "nama_mahasiswa": ["nama_mahasiswa", 139],
            "judul_skripsi": ["judul_skripsi", 139],
            "nidn": ["nidn", 139],
            "file_skripsi": ["file_skripsi", 139],
            "tanggal": ["tanggal", 139],
        }
        self._treeview_2 = Treeview(
            self,
            columns=list(self._columns_2.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            # ="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )

        for idx, txt in self._columns_2.items():
            self._treeview_2.heading(idx, text=txt[0])
            # Set the column widths
            self._treeview_2.column(idx, width=txt[1])

        self._treeview_2.place(x=62.0, y=327.0, width=975.0, height=262.5)
        self.handle_refresh_bmbg()
        #self.treeview_2.bind("<ButtonRelease-1>", self.on_treeview_click)

    def handle_refresh_mng(self):
        self._treeview.delete(*self._treeview.get_children())
        self.mng_data = db_controller.view_mng(self.user_nidn)
        for row in self.mng_data:
            self._treeview.insert("", "end", values=row)

    def handle_refresh_bmbg(self):
        self._treeview_2.delete(*self._treeview_2.get_children())
        self._bmbg_data = db_controller.view_pengajuan_bmbg(self.user_nidn)

        for row in self._bmbg_data:
            if isinstance(row[5], bytes):
                detected_encoding = self.detect_encoding(row[5])
                if detected_encoding:
                    try:
                        row = list(row)
                        row[5] = row[5].decode(detected_encoding)
                    except UnicodeDecodeError as e:
                        # Log the decoding error
                        logging.error(f"Error decoding BLOB data: {e}")
                        row = list(row)  # Convert to list to modify
                        row[5] = "Decoding Error"
                        row = tuple(row)  # Convert back to tuple
                else:
                    row = list(row)  # Convert to list to modify
                    row[5] = "Unknown Encoding"
                    row = tuple(row)  # Convert back to tuple
            self._treeview_2.insert("", "end", values=row)    
    
    def detect_encoding(self, blob_data):
        result = chardet.detect(blob_data)
        return result['encoding']   
    
    def navigate_to_modul(self):
        selected_item = self._treeview_2.selection()
        if selected_item:
            selected_data = self._treeview_2.item(selected_item)['values']
            user_nidn = selected_data[4]
            npm = selected_data[1]
            id_bimbingan_mahasiswa = selected_data[0]
            file_skripsi = selected_data[5] 
            self.parent.show_modul_pembimbing_dosen(user_nidn, npm, id_bimbingan_mahasiswa, file_skripsi)
