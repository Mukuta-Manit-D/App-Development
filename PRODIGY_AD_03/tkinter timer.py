import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        # Initialize variables for time
        self.running = False
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

        # Display Label
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), bg="black", fg="white")
        self.time_label.pack(pady=20)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start, width=10)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause, width=10)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, width=10)
        self.reset_button.grid(row=0, column=2, padx=5)

    def update_time(self):
        if self.running:
            self.milliseconds += 1
            if self.milliseconds == 100:  # Every 100 milliseconds, increase seconds
                self.milliseconds = 0
                self.seconds += 1
            if self.seconds == 60:  # Every 60 seconds, increase minutes
                self.seconds = 0
                self.minutes += 1

            # Update time display
            time_string = f"{self.minutes:02}:{self.seconds:02}:{self.milliseconds:02}"
            self.time_label.config(text=time_string)

            # Repeat every 10 ms to simulate real-time counting
            self.root.after(10, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.minutes, self.seconds, self.milliseconds = 0, 0, 0
        self.time_label.config(text="00:00:00")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
