import tkinter as tk
from tkinter import messagebox
import asyncio
from constants.global_variable import *
from feature.product.services.product_services import ProductServices
from feature.product.services.order_services import OrderServices
from models.product import Product
from feature.product.widgets.drink_tile import DrinkTile

# Function to create drink widgets
async def create_drink_widgets_async():
    loading_label = tk.Label(drinks_frame, text="Loading...")
    loading_label.grid(row=0, column=0)

    product_data = await ProductServices.fetch_coffee_data_async()

    loading_label.destroy()  # Remove loading label once data is fetched

    for i, drink_data in enumerate(product_data):
        drink = Product(
            id = drink_data["_id"],
            name=drink_data["name"],
            description=drink_data["description"],
            price=drink_data["price"],
            image_url=drink_data["image"]
        )

        frame = tk.Frame(drinks_frame, bg="white")
        frame.grid(row=i, column=0, padx=10, pady=10)

        # # Create drink image label
        # image_label = tk.Label(frame, image=drink.tk_image)
        # image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        # # Create drink name label
        # name_label = tk.Label(frame, text=drink.name)
        # name_label.grid(row=0, column=1, sticky="w")

        # # Create drink description label
        # description_label = tk.Label(frame, text=drink.description)
        # description_label.grid(row=1, column=1, sticky="w")

        # # Create drink price label
        # price_label = tk.Label(frame, text=f"Price: ${drink.price:.2f}")
        # price_label.grid(row=2, column=1, sticky="w")

        # # Create drink selection check button
        # drink.var = tk.IntVar()
        # selection_checkbutton = tk.Checkbutton(frame, variable=drink.var)
        # selection_checkbutton.grid(row=0, column=2, rowspan=3)
         
        # Use the DrinkTile class to create drink widgets
        DrinkTile(
            parent=frame,
            drink_id = drink.id,
            drink_flavour=drink.name,
            drink_price=drink.price,
            drink_description=drink.description,
            drink_image=drink.image_url
        )
        print(drink.image_url);

# Create the main window
window = tk.Tk()
window.title("Coffee Order App")
window.configure(background="white")

# Set main window to maximum screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}+0+0")

# Create drinks frame
drinks_frame = tk.Frame(window, bg="white")
drinks_frame.pack(pady=10)

# Create drink widgets asynchronously
loop = asyncio.get_event_loop()       
loop.run_until_complete(create_drink_widgets_async())

# Run the application
window.mainloop()
