import tkinter as tk

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro")
        self.time_label = tk.Label(master, text="00:00:00")
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Iniciar", command=self.start)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Parar", command=self.stop)
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Resetar", command=self.reset)
        self.reset_button.pack()

        self.running = False
        self.time = "00:00:00"

    def update_time(self):
        if self.running:
            hours, minutes, seconds = map(int, self.time.split(':'))
            seconds += 1
            if seconds == 60:
                minutes += 1
                seconds = 0
            if minutes == 60:
                hours += 1
                minutes = 0
            self.time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=self.time)
            self.master.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.time = "00:00:00"
        self.time_label.config(text=self.time)
        self.stop()

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()