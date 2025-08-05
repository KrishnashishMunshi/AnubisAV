import psutil
from tkinter import *
import tkinter as tk
from tkinter import ttk, font
from PIL import  ImageTk,Image
thisPage = 2

root = Tk()
root.title("Anubis Antivirus")
root.geometry("1270x720")


root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")


#  Colors
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26262C"


# For the Nav buttons
def hoverMenuButtons(event,i):
    global buttonsMain

    if (i == 0):
        # Mont
        buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
        buttonsMain[i].place(relx=0.05,rely=0.4)

    elif (i == 1):
        # Sec
        buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
        buttonsMain[i].place(relx=0.064,rely=0.44)
    elif (i == 2):
        # Update
        buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
        buttonsMain[i].place(relx=0.065,rely=0.49)
    elif (i == 3):
        # Tasks
        buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
        buttonsMain[i].place(relx=0.069,rely=0.54)
    elif (i == 4):
        # License
        buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
        buttonsMain[i].place(relx=0.063,rely=0.58)


def leaveMenuButtons(event, i):
    global buttonsMain
    if (i == 0):
        # Orgional place
        root.after(50)
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.4)
    elif (i == 1):
        # Orgional place
        root.after(50)
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.075, rely=0.45)
    elif (i == 2):
        # Orgional place
        root.after(50)
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.075, rely=0.50)
    elif (i == 3):
        # Orgional place
        root.after(50)
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.078, rely=0.55)
    elif (i == 4):
        # Orgional place
        root.after(50)
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.074, rely=0.595)


def nextPage(i):
    if i == 0 and thisPage != 1:
        root.destroy()
        import page1
    elif i == 1 and thisPage != 2:
        root.destroy()
        import page2
    elif i == 2 and thisPage != 3:
        root.destroy()
        import page3
    elif i == 3 and thisPage != 4:
        root.destroy()
        import page4
    elif i == 4 and thisPage != 5:
        root.destroy()
        import page5


def scanner():
    def update_progress_label(value):
        return f"Current Progress: {value}%"
    def progress(value):
        if value <= 100:
            progress_bar['value'] = value
            label.config(text=update_progress_label(value))
            root.after(1000, lambda: progress(value + 10))
        else:
            progress_bar.stop()

    top = Toplevel()
    top.title("Scanning")
    top.geometry("600x600")
    top.configure(bg="#131314")
    progress_bar = ttk.Progressbar(top, orient='horizontal', mode='determinate', length=400)
    progress_bar.place(relx= 0.15,rely=0.35)
    label = Label(top, text=update_progress_label(0), font=("Lucida Sans",12), fg= active_color, bg= backgroundColor)
    label.place(relx=0.33, rely=0.4)
    start_button = Button(top, text="Progress", fg=active_color, bg=backgroundColor, font=("Lucida Sans",12), command=lambda: progress(0))
    start_button.place(relx=0.4, rely=0.45)











image_frame = ImageTk.PhotoImage(Image.open("1x/Panel.png"))
main_frame = tk.Frame(root,bg="black")
main_frame.pack(side=tk.LEFT, fill=tk.Y)
main_frame.pack_propagate(FALSE)
main_frame.configure(width=275,height=720)

label = Label(main_frame, image= image_frame, borderwidth=0)
label.pack()

# SCAN box
img_scan = ImageTk.PhotoImage(Image.open("1x/scan.png"))
#Label(root, image= img_scan,  borderwidth=0).place(relx= 0.34, rely=0.15)
button_scan = Button(root,image=img_scan,bg=backgroundColor,width=671, borderwidth=0, height=436 , command= scanner, activebackground=backgroundColor).place(relx=0.35, rely=0.16)





# The Name of the Program

nameAnti = Label(
    root,
    text="Anubis",
    font=('Century Gothic',30,"bold"),
    bg=backgroundColor,
    fg=active_color,
    pady=0,
    padx=0
)

nameAnti.place(
    relx=0.02,
    rely=0.08
)


desAnti = Label(
    root,
    text="Endpoint Security",
    font=('Century Gothic',13),
    bg=backgroundColor,
    fg="#5A5A5B",
    pady=0,
    padx=0
)

desAnti.place(
    relx=0.02,
    rely=0.155
)



# Nav buttons
buttonsMain = ["button_monitoring","button_security","button_update","button_task","button_license" ]

buttonsMain[0] = Button(
    root,
    text="Monitoring",
    font=("Lucida Sans",12),
    fg=not_active_color,
    bg= backgroundColor,
    activebackground=backgroundColor,
    highlightthickness=0,
    borderwidth=0,
    command=lambda: nextPage(0)

)


buttonsMain[0].place(
    relx=0.07,
    rely=0.4
)


buttonsMain[1] = Button(
    root,
    text="Security",
    font=("Lucida Sans",12, "bold"),
    fg=active_color,
    bg= backgroundColor,
    activebackground=backgroundColor,
    highlightthickness=0,
    borderwidth=0,
    command = lambda : nextPage(1)
)

buttonsMain[1].place(
    relx=0.075,
    rely=0.45
)


buttonsMain[2] = Button(
    root,
    text="Update",
    font=("Lucida Sans",12),
    fg=not_active_color,
    bg= backgroundColor,
    activebackground=backgroundColor,
    highlightthickness=0,
    borderwidth=0,
    command=lambda: nextPage(2)

)

buttonsMain[2].place(
    relx=0.075,
    rely=0.50
)



buttonsMain[3] = Button(
    root,
    text="Tasks",
    font=("Lucida Sans",12),
    fg=not_active_color,
    bg= backgroundColor,
    activebackground=backgroundColor,
    highlightthickness=0,
    borderwidth=0,
    command=lambda: nextPage(3)

)

buttonsMain[3].place(
    relx=0.078,
    rely=0.55
)


buttonsMain[4] = Button(
    root,
    text="License",
    font=("Lucida Sans",12),
    fg=not_active_color,
    bg= backgroundColor,
    activebackground= backgroundColor,
    highlightthickness=0,
    borderwidth=0,
    command=lambda: nextPage(4)

)

buttonsMain[4].place(
    relx=0.074,
    rely=0.595
)



buttonsMain[0].bind("<Enter>", lambda event, i=0: hoverMenuButtons(event, i))
buttonsMain[0].bind("<Leave>", lambda event, i=0: leaveMenuButtons(event, i))



buttonsMain[1].bind("<Enter>", lambda event, i=1: hoverMenuButtons(event, i))
buttonsMain[1].bind("<Leave>", lambda event, i=1: leaveMenuButtons(event, i))

buttonsMain[2].bind("<Enter>", lambda event, i=2: hoverMenuButtons(event, i))
buttonsMain[2].bind("<Leave>", lambda event, i=2: leaveMenuButtons(event, i))

buttonsMain[3].bind("<Enter>", lambda event, i=3: hoverMenuButtons(event, i))
buttonsMain[3].bind("<Leave>", lambda event, i=3: leaveMenuButtons(event, i))

buttonsMain[4].bind("<Enter>", lambda event, i=4: hoverMenuButtons(event, i))
buttonsMain[4].bind("<Leave>", lambda event, i=4: leaveMenuButtons(event, i))


root.mainloop()
