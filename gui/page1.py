import psutil
from tkinter import *
import tkinter as tk
from tkinter import ttk, font
from PIL import  ImageTk,Image
thisPage = 1

root = Tk()
root.title("Anubis Antivirus")
root.geometry("1270x720")

#root.attributes("-alpha", 0.98)

#root.overrideredirect(True)

#def move_app(e):
    #root.geometry(f'{e.x_root}+{e.y_root}')

#title_bar = Frame(root, bg="darkgreen", relief="raised", bd=1)
#title_bar.pack(expand=1, fill=X)
# Bind the titlebar
#title_bar.bind("<B1-Motion>", move_app)


#title_label = Label(title_bar, text="   My Awesome App!!", bg="darkgreen", fg="white", bd=0)
#title_label.pack(side=LEFT, pady=4)

#close_button = Button(root, text="CLOSE", command=root.quit)
#close_button.pack(pady=100)




root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")



#  Colors
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26262C"





def update_label(label):
# This for inilizting the CPU Perecnt
    cpu_usage = psutil.cpu_percent(interval=0.1)
    ram_usage = psutil.virtual_memory().percent
# This to make it appear
    info_text = f"CPU Usage: {cpu_usage}%\nRAM Usage: {ram_usage}%"

    label.config(text=info_text)

    root.after(300, lambda: update_label(label))

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
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.4)
    elif (i == 1):
        # Orgional place
        root.after(50)
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
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


image_frame = ImageTk.PhotoImage(Image.open("../assets/1x/Panel.png"))
main_frame = tk.Frame(root,bg="black")
main_frame.pack(side=tk.LEFT, fill=tk.Y)
main_frame.pack_propagate(FALSE)
main_frame.configure(width=275,height=720)

label = Label(main_frame, image= image_frame, borderwidth=0)
label.pack()

imgAnti = ImageTk.PhotoImage(Image.open("../assets/1x/AntiPanel.png"))

canvas = Canvas(root, bg="#131314", highlightthickness=0)

labelAnti = Label(root,fg="white",image= imgAnti, borderwidth=0)
labelAnti.pack(pady=20)



textAnit = Label(root, text="No active threats\n found",font=('Lucida Sans',27,'bold'),bg="#001C24",fg="white",justify="left")
textAnit.place(
    relx = 0.72,
    rely = 0.2,
    anchor = "center"
)




#border_color = Frame(root, background="white")


C = Canvas(root,bg="#131314",width=992, height=512.5,highlightthickness=0)

C.place(
    rely=0.77,
    relx = 0.61,
    anchor = "center"
)


boxImage= ImageTk.PhotoImage(Image.open("../assets/1x/box.png"))

# The first row that contains Mid size

labelBox = Label(root,bg="#131314",image= boxImage, borderwidth=0)
labelBox.place(
    rely=0.52,
    relx = 0.409,
    anchor ="center"
)

labelBox2 = Label(root,bg="#131314",image= boxImage, borderwidth=0)
labelBox2.place(
    rely=0.52,
    relx = 0.6,
    anchor ="center"
)

labelBox3 = Label(root,bg="#131314",image= boxImage, borderwidth=0)
labelBox3.place(
    rely=0.52,
    relx = 0.8,
    anchor ="center"
)



bigBoxImage= ImageTk.PhotoImage(Image.open("../assets/1x/bigBox.png"))

# For the big Box in the left
labelBig = Label(root,bg="#131314",image= bigBoxImage, borderwidth=0)
labelBig.place(
    rely=0.77,
    relx = 0.502,
    anchor ="center"
)

text_big = Label(root,text="Anubis Antivirus", bg= backgroundColor,fg=active_color , borderwidth=0,font=("Lucida Sans",14,"bold") )
text_big.place(relx=.33,rely=0.65)

desc_big = Label(root,text="An antivirus software is a program designed to detect, prevent, and remove\n malicious software like viruses, worms, and trojans. It helps protect your system\n and personal data from cyber threats in real time.", bg= backgroundColor,fg=active_color , borderwidth=0,font=("Lucida Sans",8), justify=LEFT )
desc_big.place(relx=.33,rely=0.69)




tinyImage= ImageTk.PhotoImage(Image.open("../assets/1x/boxTiny.png"))

# For the two small boxes in the right


# For the Application
labelTiny = Label(root,bg="#131314",image= tinyImage, borderwidth=0)
labelTiny.place(
    rely=0.69,
    relx = 0.8,
    anchor ="center"
)

labelTiny.place(
    rely=0.69,
    relx = 0.8,
    anchor ="center"
)

# Application txt
text_tiny = Label(root,text="Application Activity\nMonitor", bg="#131314", fg=active_color, borderwidth=0, justify=LEFT,font=("Lucida Sans",9,"bold"))
text_tiny.place(relx = 0.72, rely=0.66)

# Application icon
app_img = ImageTk.PhotoImage(Image.open("../assets/1x/icon4.png"))
Label(root,image=app_img, bg= backgroundColor).place(relx=0.848,rely=0.658)


# Box for Network
labelTiny2 = Label(root,bg="#131314",image= tinyImage, borderwidth=0)
labelTiny2.place(
    rely=0.82,
    relx=0.8,
    anchor ="center"
)

# TXT for Network
text_tiny2 = Label(root,text="Network Monitor", bg="#131314", fg=active_color, borderwidth=0, justify=LEFT,font=("Lucida Sans",9,"bold"))
text_tiny2.place(relx = 0.72, rely=0.8)

# Network icon
net_img = ImageTk.PhotoImage(Image.open("../assets/1x/icon5.png"))
Label(root,image=net_img, bg= backgroundColor).place(relx=0.848,rely=0.787)




# for the upper boxes (Report)
text_Info = Label(root, text="Reports",bg= box_background, fg= active_color, font=("Lucida Sans",11,"bold"))
text_Info.place(
    relx=0.34,
    rely=0.46
)

# Icon for Report
report_img = ImageTk.PhotoImage(Image.open("../assets/1x/icon1.png"))

Label(root,image=report_img, bg= box_background).place(relx=0.458,rely=0.45)

# CPU & RAM Information:
info_label = Label(root, bg= box_background, fg= "#989899", font=("Lucida Sans",11,"bold"),justify=LEFT)
info_label.place(
    relx=0.35,
    rely=0.517
)

update_label(info_label)


# For the (Backup) box
button_Info2 = Button(root,bg= box_background, fg= active_color, font=("Lucida Sans",11,"bold"),activebackground= box_background, borderwidth=0, activeforeground= active_color, padx=97, pady=45)
button_Info2.place(
    relx=0.52,
    rely=0.443
)

# Icon for Backup
backup_img = ImageTk.PhotoImage(Image.open("../assets/1x/icon2.png"))

Label(root,image=backup_img, bg= box_background).place(relx=0.65,rely=0.45)

# BackUp txt

text_Info2 = Label(root, text="Backup", fg= active_color, font=("Lucida Sans",11,"bold"), bg= box_background)
text_Info2.place(
    relx=0.53,
    rely=0.463
)

# For the Threat box
button_Info3 = Button(root,bg= box_background,borderwidth=0, fg= active_color, font=("Lucida Sans",11,"bold"),activebackground= box_background, activeforeground= active_color, padx=97, pady=45)
button_Info3.place(
    relx=0.72,
    rely=0.443
)

# Threat txt

text_Info3 = Label(root, text="Threat detection\ntechnologies", fg= active_color, font=("Lucida Sans",12,"bold"), bg= box_background, justify=LEFT)
text_Info3.place(
    relx=0.726,
    rely=0.463
)

# Icon for Threat
threat_img = ImageTk.PhotoImage(Image.open("../assets/1x/icon3.png"))

Label(root,image=threat_img, bg= box_background).place(relx=0.848,rely=0.45)




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






# Nav Buttons

buttonsMain = ["button_monitoring","button_security","button_update","button_task","button_license" ]

buttonsMain[0] = Button(
    root,
    text="Monitoring",
    font=("Lucida Sans",12, "bold"),
    fg=active_color,
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
    font=("Lucida Sans",12),
    fg=not_active_color,
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
