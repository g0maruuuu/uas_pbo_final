import tkinter as tk
#from guiii.main_page_admin.gui import mainPageAdmin
#from guiii.main_page.gui import mainpage
#from guiii.login_page.gui import login
from guiii.landing_page.gui import landingpage

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":
    
    #mainpage()
    #mainPageAdmin()
    #login()
    landingpage()

    root.mainloop()
