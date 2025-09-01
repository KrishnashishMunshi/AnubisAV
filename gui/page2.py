import psutil
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import threading
import time
import random
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from classify import initialize_classifier, get_malice_score

thisPage = 2
initialize_classifier()
root = tk.Tk()
root.title("Anubis Antivirus")
root.geometry("1270x720")
root.configure(bg="#131314")

# Colors
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"

# Log messages from second code
LOG_MESSAGES = [
    "Initializing scan engine...",
    "Loading signature database...",
    "Analyzing file headers...",
    "Checking for known vulnerabilities...",
    "Scanning for suspicious patterns...",
    "Performing heuristic analysis...",
    "Checking for polymorphic code...",
    "Analyzing memory allocation...",
    "Decompressing archives for inspection...",
    "Finalizing report...",
]

# ------------------- Navigation Buttons -------------------
def hoverMenuButtons(event, i):
    if i == 0:
        buttonsMain[i].config(font=("Lucida Sans", 16, "bold"), bg=backgroundColor, fg="#DEDEE0")
        buttonsMain[i].place(relx=0.05, rely=0.4)
    elif i == 1:
        buttonsMain[i].config(font=("Lucida Sans", 16, "bold"), bg=backgroundColor, fg="#DEDEE0")
        buttonsMain[i].place(relx=0.064, rely=0.44)
    elif i == 2:
        buttonsMain[i].config(font=("Lucida Sans", 16, "bold"), bg=backgroundColor, fg="#DEDEE0")
        buttonsMain[i].place(relx=0.065, rely=0.49)
    elif i == 3:
        buttonsMain[i].config(font=("Lucida Sans", 16, "bold"), bg=backgroundColor, fg="#DEDEE0")
        buttonsMain[i].place(relx=0.069, rely=0.54)
    elif i == 4:
        buttonsMain[i].config(font=("Lucida Sans", 16, "bold"), bg=backgroundColor, fg="#DEDEE0")
        buttonsMain[i].place(relx=0.063, rely=0.58)

def leaveMenuButtons(event, i):
    if i == 0:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.4)
    elif i == 1:
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.075, rely=0.45)
    elif i == 2:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.075, rely=0.50)
    elif i == 3:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.078, rely=0.55)
    elif i == 4:
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

# ------------------- Modern Scan UI from Code 2 -------------------
# --- Main Scanner Window Function ---
def scanner():
    # --- Define Colors and Messages ---
    # (Assuming these are defined somewhere, or you can define them here)
    backgroundColor = "#2b2b2b"
    active_color = "#cccccc"
    LOG_MESSAGES = [
        "Initializing scan engine...",
        "Parsing PE headers...",
        "Analyzing import address table...",
        "Scanning .text section...",
        "Checking for known signatures...",
        "Analyzing resource section...",
        "Heuristic analysis in progress...",
        "Finalizing feature extraction...",
        "Sending data to classifier...",
        "Compiling final report..."
    ]

    selected_file = {"path": None}
    scanning = {"status": False}
    elapsed_time = {"seconds": 0}

    def browse_file():
        path = filedialog.askopenfilename(
            title="Select a Windows Executable",
            filetypes=[("Executable files", "*.exe"), ("All files", "*.*")]
        )
        if path:
            selected_file["path"] = path
            file_label.config(text=f"File: {os.path.basename(path)}", fg=active_color)
            start_button.config(state="normal")

    def update_system_stats():
        while scanning["status"]:
            try:
                cpu = psutil.cpu_percent(interval=0.5)
                mem = psutil.virtual_memory().percent
                cpu_label.config(text=f"CPU Usage: {cpu}%")
                mem_label.config(text=f"Memory Usage: {mem}%")
                time.sleep(0.5)
            except (tk.TclError, RuntimeError): # Catch errors if window is closed
                break

    def update_timer():
        while scanning["status"]:
            try:
                time.sleep(1)
                elapsed_time["seconds"] += 1
                mins, secs = divmod(elapsed_time["seconds"], 60)
                timer_label.config(text=f"Elapsed Time: {mins:02}:{secs:02}")
            except (tk.TclError, RuntimeError):
                break

    def run_analysis():
        """Calls the backend, stops the UI monitors, and displays the result."""
        log_box.config(state="normal")
        log_box.insert(tk.END, "> Running ML model...\n")
        log_box.see(tk.END)
        score = get_malice_score(selected_file["path"])

        scanning["status"] = False
        progress_bar.stop()
        progress_bar['mode'] = 'determinate'
        progress_bar["value"] = 100
        progress_label.config(text="Scan Complete")
        log_box.insert(tk.END, "> Analysis finished.\n")
        log_box.see(tk.END)
        log_box.config(state="disabled")

        if score is None:
            result_label.config(text=f"Error analyzing file.", fg="orange")
        elif score == -1.0:
            result_label.config(text=f"File is not a valid Windows executable.", fg="orange")
        elif score > 0.7:
            result_label.config(text=f"Threat DETECTED! Malice Score: {score:.4f}", fg="#ff4d4d")
        else:
            result_label.config(text=f"No threats found. Malice Score: {score:.4f}", fg="#4dff4d")

        start_button.config(state="normal")

    def start_scan_thread():
        """Prepares the UI and starts the analysis in a new thread."""
        if not selected_file["path"]:
            return

        scanning["status"] = True
        elapsed_time["seconds"] = 0
        start_button.config(state="disabled")

        result_label.config(text="Analyzing...", fg=active_color)
        timer_label.config(text="Elapsed Time: 00:00")
        progress_label.config(text="Current Progress: Analyzing...")
        log_box.config(state="normal")
        log_box.delete("1.0", tk.END)
        log_box.insert(tk.END, f"> Starting scan for: {os.path.basename(selected_file['path'])}\n")
        log_box.config(state="disabled")

        progress_bar['mode'] = 'indeterminate'
        progress_bar.start(10)

        threading.Thread(target=update_system_stats, daemon=True).start()
        threading.Thread(target=update_timer, daemon=True).start()
        threading.Thread(target=run_analysis, daemon=True).start()

    # --- GUI Widget Setup (Corrected Syntax) ---
    top = tk.Toplevel()
    top.title("AnubisAV Static Analysis")
    top.geometry("800x650")
    top.configure(bg=backgroundColor)

    upload_btn = tk.Button(top, text="Select File", font=("Lucida Sans", 12), fg=active_color, bg=backgroundColor, command=browse_file)
    upload_btn.pack(pady=10)

    file_label = tk.Label(top, text="No file selected", font=("Lucida Sans", 12), fg="grey", bg=backgroundColor)
    file_label.pack()

    progress_bar = ttk.Progressbar(top, orient='horizontal', mode='determinate', length=500)
    progress_bar.pack(pady=10)

    progress_label = tk.Label(top, text="Current Progress: 0%", font=("Lucida Sans", 12), fg=active_color, bg=backgroundColor)
    progress_label.pack()

    cpu_label = tk.Label(top, text="CPU Usage: 0%", font=("Lucida Sans", 12), fg=active_color, bg=backgroundColor)
    cpu_label.pack()

    mem_label = tk.Label(top, text="Memory Usage: 0%", font=("Lucida Sans", 12), fg=active_color, bg=backgroundColor)
    mem_label.pack()

    timer_label = tk.Label(top, text="Elapsed Time: 00:00", font=("Lucida Sans", 12), fg=active_color, bg=backgroundColor)
    timer_label.pack()

    log_box = tk.Text(top, height=15, bg="#1a1a1a", fg="white", font=("Consolas", 10), state="disabled")
    log_box.pack(pady=10, padx=20, fill="x")

    result_label = tk.Label(top, text="", font=("Lucida Sans", 14, "bold"), bg=backgroundColor)
    result_label.pack(pady=10)

    start_button = tk.Button(top, text="Start Scan", fg=active_color, bg=backgroundColor, font=("Lucida Sans", 12), command=start_scan_thread, state="disabled")
    start_button.pack(pady=10)


# ------------------- Left Panel -------------------
image_frame = ImageTk.PhotoImage(Image.open("../assets/1x/Panel.png"))
main_frame = tk.Frame(root, bg="black", width=275, height=720)
main_frame.pack(side=tk.LEFT, fill=tk.Y)
main_frame.pack_propagate(False)

label = tk.Label(main_frame, image=image_frame, borderwidth=0)
label.pack()

# Scan button
img_scan = ImageTk.PhotoImage(Image.open("../assets/1x/scan.png"))
tk.Button(root, image=img_scan, bg=backgroundColor, width=671, borderwidth=0, height=436,
          command=scanner, activebackground=backgroundColor).place(relx=0.35, rely=0.16)

# Program name
nameAnti = tk.Label(root, text="Anubis", font=('Century Gothic', 30, "bold"), bg=backgroundColor, fg=active_color)
nameAnti.place(relx=0.02, rely=0.08)

desAnti = tk.Label(root, text="Endpoint Security", font=('Century Gothic', 13), bg=backgroundColor, fg="#5A5A5B")
desAnti.place(relx=0.02, rely=0.155)

# Navigation buttons
buttonsMain = [""] * 5
nav_texts = ["Monitoring", "Security", "Update", "Tasks", "License"]
nav_commands = [lambda: nextPage(0), lambda: nextPage(1), lambda: nextPage(2), lambda: nextPage(3), lambda: nextPage(4)]

for idx, text in enumerate(nav_texts):
    font_style = ("Lucida Sans", 12, "bold") if idx == 1 else ("Lucida Sans", 12)
    fg_color = active_color if idx == 1 else not_active_color
    buttonsMain[idx] = tk.Button(
        root, text=text, font=font_style, fg=fg_color, bg=backgroundColor,
        activebackground=backgroundColor, borderwidth=0, command=nav_commands[idx]
    )
    buttonsMain[idx].place(relx=0.07 + (0.005 if idx != 0 else 0), rely=0.4 + idx * 0.05)
    buttonsMain[idx].bind("<Enter>", lambda e, i=idx: hoverMenuButtons(e, i))
    buttonsMain[idx].bind("<Leave>", lambda e, i=idx: leaveMenuButtons(e, i))

root.mainloop()
