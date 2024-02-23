import tkinter as tk
from tkinter import ttk

class Processing:
    def __init__(self):
        self = tk.Tk()
        self.title("Processing")

        # ... other initialization code ...

        self.create_progress_bar()

    def create_progress_bar(self):
        self.progress_bar_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.root, variable=self.progress_bar_var, mode='indeterminate')
        self.progress_bar.pack(pady=10)

        start_button = tk.Button(self.root, text="Start Progress", command=self.start_progress)
        start_button.pack(pady=10)

    def start_progress(self):
        self.progress_bar.start()  # Start the progress bar

        # Simulate some processing (you can replace this with your actual processing logic)
        self.root.after(3000, self.stop_progress)

    def stop_progress(self):
        self.progress_bar.stop()  # Stop the progress bar

processing = Processing()
processing.mainloop()
