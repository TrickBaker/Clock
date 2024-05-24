import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='black')

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 100), background='black', foreground='white')
        self.style.configure('TButton', font=('Helvetica', 30), padding=10)

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.label = ttk.Label(root, textvariable=self.time_var, style='TLabel')
        self.label.pack(expand=True)

        self.entry = ttk.Entry(root, font=("Helvetica", 30), width=10)
        self.entry.pack(pady=20)
        self.entry.focus()

        self.start_button = ttk.Button(root, text="Start Countdown", command=self.start_countdown, style='TButton')
        self.start_button.pack(pady=10)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset, style='TButton')
        self.reset_button.pack(pady=10)

        self.quit_button = ttk.Button(root, text="Quit", command=self.root.quit, style='TButton')
        self.quit_button.pack(pady=10)

        self.time_left = 0

    def start_countdown(self):
        try:
            t = self.entry.get()
            self.time_left = int(t.split(":")[0]) * 3600 + int(t.split(":")[1]) * 60 + int(t.split(":")[2])
            self.countdown()
        except:
            messagebox.showerror("Invalid input", "Please enter time in HH:MM:SS format")

    def countdown(self):
        if self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            hours, mins = divmod(mins, 60)
            time_format = f"{hours:02}:{mins:02}:{secs:02}"
            self.time_var.set(time_format)
            self.root.update()
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.time_var.set("00:00:00")
            messagebox.showinfo("Time's up!", "Countdown finished")

    def reset(self):
        self.time_var.set("00:00:00")
        self.time_left = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
