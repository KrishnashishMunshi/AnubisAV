
import tkinter as tk
from tkinter import filedialog, ttk
import platform
import psutil
import threading
import time
import random

class AnubisApp:
    """
    An object-oriented approach to the Anubis Antivirus GUI application.
    This class encapsulates all the UI elements, state, and logic.
    """
    def __init__(self, root):
        self.root = root
        self.setup_constants()
        self.setup_variables()
        self.setup_ui()
        self.start_background_tasks()

    def setup_constants(self):
        """Define fonts, colors, and other static values."""
        self.TITLE_FONT = ("Orbitron", 28, "bold")
        self.SCORE_FONT = ("Orbitron", 48, "bold")
        self.SUB_FONT = ("Orbitron", 14)
        self.STATUS_FONT = ("Orbitron", 12, "italic")
        self.LOG_FONT = ("Consolas", 10)
        self.TEXT_COLOR = "#00ffe1"
        self.RING_COLOR = "#00fff2"
        self.ALERT_RING_COLOR = "#ff0033"
        self.WAVE_COLOR = "#009fbd"
        self.SAFE_COLOR = "#2ecc71"
        self.WARN_COLOR = "#f1c40f"
        self.THREAT_COLOR = "#e74c3c"
        self.BG_COLOR = '#0a0f1c'
        self.LOG_BG_COLOR = '#0d1426'
        self.LOG_MESSAGES = [
            "Initializing scan engine...",
            "Loading signature database...",
            "Analyzing file headers...",
            "Checking for known vulnerabilities...",
            "Scanning for suspicious patterns...",  
            "Scanning for known malware patterns...",
            "Performing heuristic analysis...",
            "Checking for polymorphic code...",
            "Analyzing memory allocation...",
            "Decompressing archives for inspection...",
            "Finalizing report...",
        ]

    def setup_variables(self):
        """Initialize all the dynamic state variables for the application."""
        self.angle = 0
        self.system_name = platform.system()
        self.selected_file = None
        self.threat_detected = False
        self.title_pulse_state = 0
        self.is_scanning = False

    def setup_ui(self):
        """Configure the main window and create all UI widgets."""
        self.root.title("Anubis Antivirus")
        self.root.geometry("1920x10801")
        self.root.configure(bg=self.BG_COLOR)

        # --- Main Canvas for animations ---
        self.canvas = tk.Canvas(self.root, width=720, height=720, bg=self.BG_COLOR, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')
        self.center_x, self.center_y = 360, 360
        self.radius = 150

        # Static background ring
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius,
                                outline="#222", width=10)
        # Animated Progress Ring (initially hidden)
        self.progress_ring = self.canvas.create_arc(self.center_x - self.radius, self.center_y - self.radius,
                                                   self.center_x + self.radius, self.center_y + self.radius,
                                                   start=90, extent=0, outline=self.RING_COLOR, width=8, style=tk.ARC)

        # --- Canvas Text Elements ---
        self.score_text = self.canvas.create_text(self.center_x, self.center_y, text="--", fill=self.TEXT_COLOR, font=self.SCORE_FONT)
        self.status_text = self.canvas.create_text(self.center_x, self.center_y + 60, text="IDLE", fill=self.TEXT_COLOR, font=self.STATUS_FONT)
        self.cpu_text = self.canvas.create_text(self.center_x, self.center_y + 210, text="", fill=self.TEXT_COLOR, font=self.SUB_FONT)
        self.ram_text = self.canvas.create_text(self.center_x, self.center_y + 240, text="", fill=self.TEXT_COLOR, font=self.SUB_FONT)
        self.os_text = self.canvas.create_text(self.center_x, self.center_y + 270, text=f"OS: {self.system_name}", fill=self.TEXT_COLOR, font=self.SUB_FONT)

        # Animated waveform line
        self.wave_base_y = self.center_y + 310
        self.wave = self.canvas.create_line(self.center_x - 100, self.wave_base_y, self.center_x + 100, self.wave_base_y, fill=self.WAVE_COLOR, width=3, smooth=True)

        # --- Top UI Elements ---
        self.scanner_title = tk.Label(self.root, text="Anubis Antivirus", font=self.TITLE_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.scanner_title.pack(pady=5)
        self.file_label = tk.Label(self.root, text="No file selected.", font=self.SUB_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.file_label.pack(pady=5)

        # --- Analysis Log Widget ---
        self.log_frame = tk.Frame(self.root, bg=self.LOG_BG_COLOR)
        self.log_frame.pack(pady=10, padx=20, fill="x")
        self.log_text = tk.Text(self.log_frame, height=6, bg=self.LOG_BG_COLOR, fg=self.TEXT_COLOR,
                                font=self.LOG_FONT, relief="flat", insertbackground=self.TEXT_COLOR)
        self.log_text.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        self.log_text.config(state="disabled")

        # --- Bottom UI Elements ---
        self.result_label = tk.Label(self.root, text="", font=self.SUB_FONT, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.result_label.pack(side="bottom", pady=10)
        
        btn_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        btn_frame.pack(side="bottom", pady=10)
        
        self.select_file_btn = tk.Button(btn_frame, text="SELECT FILE", command=self.select_file,
                                    font=self.SUB_FONT, bg="#001d33", fg=self.TEXT_COLOR,
                                    activebackground="#003e52", activeforeground=self.TEXT_COLOR,
                                    width=15, relief="flat", borderwidth=2)
        self.select_file_btn.pack(side="left", padx=10)

        self.quick_scan_btn = tk.Button(btn_frame, text="QUICK SCAN", command=lambda: self.start_scan("quick"),
                                   font=self.SUB_FONT, bg="#003322", fg=self.TEXT_COLOR,
                                   activebackground="#005232", activeforeground=self.TEXT_COLOR,
                                   width=15, relief="flat", borderwidth=2, state="disabled")
        self.quick_scan_btn.pack(side="left", padx=10)

        self.full_scan_btn = tk.Button(btn_frame, text="FULL SCAN", command=lambda: self.start_scan("full"),
                                   font=self.SUB_FONT, bg="#332200", fg=self.TEXT_COLOR,
                                   activebackground="#523200", activeforeground=self.TEXT_COLOR,
                                   width=15, relief="flat", borderwidth=2, state="disabled")
        self.full_scan_btn.pack(side="left", padx=10)

    def start_background_tasks(self):
        threading.Thread(target=self.update_metrics, daemon=True).start()
        self.rotate_ring()
        self.update_wave()
        self.pulse_title()

    def update_metrics(self):
        while True:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            self.canvas.itemconfig(self.cpu_text, text=f"CPU Usage: {cpu}%")
            self.canvas.itemconfig(self.ram_text, text=f"RAM Usage: {ram}%")
            time.sleep(1)

    def rotate_ring(self):
        self.canvas.delete("rotating_ring")
        self.angle = (self.angle + 4) % 360
        
        x1, y1 = self.center_x - self.radius * 1.2, self.center_y - self.radius * 1.2
        x2, y2 = self.center_x + self.radius * 1.2, self.center_y + self.radius * 1.2
        
        if self.is_scanning or self.threat_detected:
            self.canvas.create_arc(x1, y1, x2, y2, start=self.angle, extent=60,
                                   outline=self.ALERT_RING_COLOR if self.threat_detected else self.WARN_COLOR, 
                                   style="arc", width=4, tags="rotating_ring")
        self.root.after(50, self.rotate_ring)

    def update_wave(self):
        amplitude = 5
        color = self.WAVE_COLOR
        if self.is_scanning:
            amplitude = 15
            color = self.WARN_COLOR
        if self.threat_detected:
            amplitude = 25
            color = self.ALERT_RING_COLOR
        
        points = [item for i in range(50) for item in (self.center_x - 100 + i * 4, self.wave_base_y + random.randint(-amplitude, amplitude))]
        self.canvas.coords(self.wave, *points)
        self.canvas.itemconfig(self.wave, fill=color)
        self.root.after(100, self.update_wave)

    def pulse_title(self):
        self.title_pulse_state = 1 - self.title_pulse_state
        self.scanner_title.config(fg="#00ffe1" if self.title_pulse_state == 0 else "#33fff8")
        self.root.after(1000, self.pulse_title)

    def select_file(self):
        if self.is_scanning: return
        self.selected_file = filedialog.askopenfilename()
        if self.selected_file:
            self.file_label.config(text=f"File: {self.selected_file.split('/')[-1]}")
            self.quick_scan_btn.config(state="normal")
            self.full_scan_btn.config(state="normal")
            self.reset_ui(keep_filename=True)

    def start_scan(self, scan_type):
        if self.is_scanning: return
        self.reset_ui(keep_filename=True)
        self.is_scanning = True
        self.toggle_buttons(False)
        self.canvas.itemconfig(self.status_text, text="ANALYZING...")
        
        scan_speed = 0.01 if scan_type == "quick" else 0.03
        threading.Thread(target=self.simulate_scan, args=(scan_speed,), daemon=True).start()
        threading.Thread(target=self.update_log, args=(scan_speed,), daemon=True).start()

    def simulate_scan(self, speed):
        for i in range(101):
            time.sleep(speed)
            progress_angle = i * 3.6
            self.canvas.itemconfig(self.progress_ring, extent=progress_angle)
            self.canvas.itemconfig(self.score_text, text=f"{i}%")
        
        threat_score = random.randint(0, 100)
        self.root.after(0, self.display_scan_results, threat_score)

    def update_log(self, speed):
        self.log_text.config(state="normal")
        self.log_text.delete('1.0', tk.END)
        for message in self.LOG_MESSAGES:
            if not self.is_scanning: break
            self.log_text.insert(tk.END, f"> {message}\n")
            self.log_text.see(tk.END)
            time.sleep(speed * 10)
        self.log_text.config(state="disabled")

    def display_scan_results(self, score):
        self.is_scanning = False
        self.toggle_buttons(True)
        self.threat_detected = score > 70

        score_color = self.SAFE_COLOR
        if 40 <= score <= 70: score_color = self.WARN_COLOR
        elif score > 70: score_color = self.THREAT_COLOR
        self.canvas.itemconfig(self.score_text, text=f"{score}", fill=score_color)

        if self.threat_detected:
            self.canvas.itemconfig(self.status_text, text="THREAT DETECTED", fill=self.THREAT_COLOR)
            self.result_label.config(text="Action Required: Threat has been quarantined.", fg=self.THREAT_COLOR)
        else:
            self.canvas.itemconfig(self.status_text, text="SYSTEM SECURE", fill=self.SAFE_COLOR)
            self.result_label.config(text="Scan complete. No threats were found.", fg=self.SAFE_COLOR)

    def reset_ui(self, keep_filename=False):
        self.threat_detected = False
        self.is_scanning = False
        self.canvas.itemconfig(self.progress_ring, extent=0)
        self.canvas.itemconfig(self.score_text, text="--", fill=self.TEXT_COLOR)
        self.canvas.itemconfig(self.status_text, text="IDLE", fill=self.TEXT_COLOR)
        self.result_label.config(text="")
        if not keep_filename:
            self.file_label.config(text="No file selected.")

    def toggle_buttons(self, enabled):
        state = "normal" if enabled else "disabled"
        self.select_file_btn.config(state=state)
        if self.selected_file:
            self.quick_scan_btn.config(state=state)
            self.full_scan_btn.config(state=state)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnubisApp(root)
    root.mainloop()
