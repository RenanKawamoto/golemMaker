from tkinter.ttk import Style
from os import getenv

def global_style_config(root):
    global_style = Style(root)
    FIRST_COLOR = getenv("FIRST_COLOR")
    SECOND_COLOR = getenv("SECOND_COLOR")
    THIRD_COLOR = getenv("THIRD_COLOR")
    FOURTH_COLOR = getenv("FOURTH_COLOR")
    
    #--------------------------THEME----------------------------#
    global_style.theme_use("default")
    #-----------------------------------------------------------#
    
    #--------------------------TFrame---------------------------#
    global_style.configure("TFrame", background=FIRST_COLOR)
    #-----------------------------------------------------------#
    
    #--------------------------TCanvas--------------------------#
    global_style.configure("TCanvas", background=FIRST_COLOR)
    #-----------------------------------------------------------#
    
     #------------------------TScrollbar------------------------#
    global_style.configure("TScrollbar", background=SECOND_COLOR, troughcolor=FIRST_COLOR, arrowcolor=THIRD_COLOR)
    
    global_style.map("Vertical.TScrollbar",
        background=[("active", SECOND_COLOR)],
        troughcolor=[("active", FIRST_COLOR)],
        arrowcolor=[("active", FOURTH_COLOR)]
    )
    #-----------------------------------------------------------#
    
    #--------------------------TButton--------------------------#
    global_style.configure("TButton", background=THIRD_COLOR, foreground=FIRST_COLOR, relief="flat", font=("calibri", 15))
    
    global_style.map("TButton",
        background=[("active", SECOND_COLOR)],
        foreground=[("active", "white")],
    )
    #-----------------------------------------------------------#
    
    #--------------------------TLabel---------------------------#
    global_style.configure("TLabel", background=FIRST_COLOR, foreground=THIRD_COLOR)
    #-----------------------------------------------------------#
    
    #-------------------------H1.TLabel-------------------------#
    global_style.configure("H1.TLabel", background=FIRST_COLOR, foreground=THIRD_COLOR, font=("Josefin Sans", 22, "bold"))
    #-----------------------------------------------------------#
    
    #----------------------Subtitle.TLabel----------------------#
    global_style.configure("Subtitle.TLabel", background=FIRST_COLOR, foreground=SECOND_COLOR, font=("calibri", 12, "italic"))
    #-----------------------------------------------------------#
    
    #----------------------------TEntry-------------------------#
    global_style.configure("TEntry", foreground=FOURTH_COLOR, fieldbackground=FIRST_COLOR ,font=("calibri", 29, "italic"))
    #-----------------------------------------------------------#
    
    
    