import tkinter as tk
from guiii.main_page_admin.gui import mainPageAdmin
from guiii.main_page.gui import mainpage

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    #mainpage()
    mainPageAdmin()
   

    root.mainloop()
