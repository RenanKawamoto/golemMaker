from tkinter.ttk import Style

def global_style_config(root):
    global_style = Style(root)
    
    #--------------------------THEME----------------------------#
    global_style.theme_use("default")
    #-----------------------------------------------------------#
    
    #--------------------------TFrame---------------------------#
    global_style.configure("TFrame", background="#F2ECBE")
    #-----------------------------------------------------------#
    
    #--------------------------TButton--------------------------#
    global_style.configure("TButton", background="#C08261", foreground="#F2ECBE", relief="flat")
    
    global_style.map("TButton",
        background=[("active", "#E2C799")],
        foreground=[("active", "white")],
    )
    #-----------------------------------------------------------#
    
    
    #--------------------------TLabel---------------------------#
    global_style.configure("TLabel", background="#F2ECBE")
    #-----------------------------------------------------------#