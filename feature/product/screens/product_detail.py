from io import BytesIO
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
# import processing as ps

import requests

from feature.product.services.order_services import OrderServices

class ProductDetailScreen(tk.Toplevel):
    def __init__(self, parent, id, name, price, description, image):
        super().__init__(parent)
        self.title("Product Detail")
        
        self.configure(background="white")

        # Set main window to maximum screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.quantity = 1

        # Heading
        heading_frame = tk.Frame(self, bg="white")
        heading_frame.pack(pady=10)
        tk.Button(heading_frame, text="Back", command=self.go_back, bg="white").pack(side=tk.LEFT)
        tk.Label(heading_frame, text=f"Item Detail", font=("Niradei", 24, "bold"), bg="white").pack(side=tk.LEFT, padx=10)

        image_frame = tk.Frame(self, bg="white")
        image_frame.pack(pady=10)
        # Load drink image from Cloudinary URL
        image = self.load_image_from_url(self.image)
        image_label = ttk.Label(image_frame, image=image)
        image_label.image = image
        image_label.grid(row=0, column=0, rowspan=2, padx=12, pady=12)

        # Drink name and price
        name_frame = tk.Frame(self)
        name_frame.pack(pady=10)
        tk.Label(name_frame, text=self.name, font=("Niradei", 24, "bold"), bg="white").pack(side=tk.LEFT)
        
        price_frame = tk.Frame(self)
        price_frame.pack(pady=10)
        tk.Label(price_frame, text=f"${self.price:.2f}", font=("Niradei", 24, "bold"), bg="white").pack(side=tk.LEFT)

        # Drink description
        description_frame = tk.Frame(self)
        description_text = tk.Text(description_frame, wrap=tk.WORD, width=40, height=6)
        description_text.insert(tk.END, self.description)
        description_text.config(state=tk.DISABLED)
        description_frame.pack(pady=10)
        description_text.pack()

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
        print("Button clicked! Going back.")
        self.destroy()

        # pass

    def handle_quantity_changed(self):
        self.quantity = int(self.quantity_var.get())

    # Function to load image from URL
    def load_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((100, 100), Image.ADAPTIVE)
        return ImageTk.PhotoImage(img)
    
    # Function to place an order
    def place_order(self):
        total_price = self.quantity * self.price
        OrderServices.placeOrder(self.id, self.quantity, total_price)
        # psbar = ps.Processing()
        # frame = tk.Frame(psbar, bg="white")



    


