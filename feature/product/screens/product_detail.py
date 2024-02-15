import tkinter as tk
from tkinter import ttk

class ProductDetailScreen(tk.Toplevel):
    def __init__(self, parent ,name, description, price, image):
        super().__init__(parent)
        self.title("Product Detail")
        
        self.configure(background="white")

        # Set main window to maximum screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.quantity = 1

        # Heading
        heading_frame = tk.Frame(self)
        heading_frame.pack(pady=10)
        tk.Button(heading_frame, text="Back", command=self.go_back).pack(side=tk.LEFT)
        tk.Label(heading_frame, text=f"Item Detail", font=("Niradei", 24, "bold")).pack(side=tk.LEFT, padx=10)


        # Drink name and price
        name_frame = tk.Frame(self)
        name_frame.pack(pady=10)
        tk.Label(name_frame, text=self.name, font=("Niradei", 24, "bold")).pack(side=tk.LEFT)
        
        price_frame = tk.Frame(self)
        price_frame.pack(pady=10)
        tk.Label(price_frame, text=self.price, font=("Niradei", 24, "bold")).pack(side=tk.LEFT)


        # Drink description
        description_frame = tk.Frame(self)
        description_frame.pack(pady=10)
        description_text = tk.Text(description_frame, wrap=tk.WORD, width=40, height=6)
        description_text.insert(tk.END, self.description)
        description_text.config(state=tk.DISABLED)

        # Add quantity
        quantity_frame = tk.Frame(self)
        quantity_frame.pack(pady=10)
        ttk.Label(quantity_frame, text="Quantity:").pack(side=tk.LEFT)
        self.quantity_var = tk.StringVar(value=self.quantity)
        quantity_spinbox = ttk.Spinbox(quantity_frame, from_=1, to=10, textvariable=self.quantity_var, command=self.handle_quantity_changed)
        quantity_spinbox.pack(side=tk.LEFT)

        # Place order button
        order_button = tk.Button(self, text="Place Order", command=self.place_order)
        order_button.pack(pady=10)

    def go_back(self):
        # Implement your logic to navigate back
        pass

    def handle_quantity_changed(self):
        self.quantity = int(self.quantity_var.get())

    def place_order(self):
        total_price = self.quantity * self.price
        print(f"Placing order for {self.name} x{self.quantity}. Total Price: ${total_price:.2f}")


