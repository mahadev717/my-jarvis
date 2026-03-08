import tkinter as tk
import math
import threading

class JarvisUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("JARVIS")
        self.root.geometry("400x400")
        self.root.configure(bg="black")
        self.root.overrideredirect(True) # Remove window borders
        
        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - 200
        y = (screen_height // 2) - 200
        self.root.geometry(f"400x400+{x}+{y}")

        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.status_label = tk.Label(self.root, text="INITIALIZING...", fg="#00ccff", bg="black", font=("Courier", 12))
        self.status_label.pack(side="bottom", pady=20)

        self.angle: float = 0.0
        self.circle_radius = 100
        self.dots = []
        self.is_active = True
        
        # Create persistent circle of dots
        for i in range(12):
            dot = self.canvas.create_oval(0, 0, 0, 0, fill="#00ffff", outline="#00ffff")
            self.dots.append(dot)

        self._animate()

    def update_status(self, text: str):
        self.status_label.config(text=text.upper())

    def _animate(self):
        if not self.is_active:
            return

        self.angle += 0.05
        for i, dot in enumerate(self.dots):
            # Calculate position
            theta = self.angle + (i * (2 * math.pi / 12))
            # Oscillating radius for "breathing" effect
            r = self.circle_radius + 10 * math.sin(self.angle * 2)
            
            x = 200 + r * math.cos(theta)
            y = 200 + r * math.sin(theta)
            
            # Update size for pulsing effect
            size = 4 + 2 * math.sin(theta + self.angle)
            self.canvas.coords(dot, x-size, y-size, x+size, y+size)
            
            # Trail color effect (optional implementation detail)
            # self.canvas.itemconfig(dot, fill=f"#{int(100+50*math.sin(theta)):02x}ffff")

        self.root.after(30, self._animate)

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.is_active = False
        self.root.destroy()

def start_ui():
    ui = JarvisUI()
    return ui
