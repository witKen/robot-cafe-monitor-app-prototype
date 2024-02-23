import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import requests
from io import BytesIO
from ..screens.product_detail import ProductDetailScreen


class DrinkTile(tk.Frame):
    def __init__(self, parent, drink_id,drink_flavour, drink_price, drink_description, drink_image):
        super().__init__(parent, bg="white", borderwidth=2, highlightbackground="red", highlightthickness=1)
        self.drink_id = drink_id
        self.drink_flavour = drink_flavour
        self.drink_price = drink_price
        self.drink_description = drink_description
        self.drink_image = drink_image

        self.create_widgets()
        self.pack()

        # Bind left mouse button click event to the show_product_detail method
        self.bind("<Button-1>", self.show_product_detail)

    # Function to load image from URL
    def load_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((100, 100), Image.ADAPTIVE)
        return ImageTk.PhotoImage(img)

    def create_widgets(self):
        # Load drink image from Cloudinary URL
        image = self.load_image_from_url(self.drink_image)
        image_label = Label(self, image=image, width=100, height=100)
        image_label.image = image
        image_label.grid(row=0, column=0, rowspan=2, padx=12, pady=12)
        image_label.bind("<Button-1>", self.show_product_detail)

        flavour_label = Label(self, text=self.drink_flavour, font=('Helvetica', 15),bg="white", padx=12)
        flavour_label.grid(row=0, column=1, sticky=tk.W)
        flavour_label.bind("<Button-1>", self.show_product_detail)

        price_label = Label(self, text=f"${self.drink_price:.2f}", font=('Helvetica', 20), bg="white", padx=12)
        price_label.grid(row=1, column=1, sticky=tk.W)
        price_label.bind("<Button-1>", self.show_product_detail)

    # Function to show the product detail screen
    def show_product_detail(self, event):
        ProductDetailScreen(self.master,self.drink_id ,self.drink_flavour, self.drink_price, self.drink_description, self.drink_image)
