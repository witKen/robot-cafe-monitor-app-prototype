import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import json
from io import BytesIO
import asyncio

coffee_drinks = []
uri = 'http://172.23.33.232:3000'

class Product:
    def __init__(self, id, name, description, price, image_url):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url
        self.var = None
        self.tk_image = None

# Function to fetch coffee drink data from the Node.js server asynchronously
async def fetch_coffee_data_async():
    try:
        response = await loop.run_in_executor(None, lambda: requests.get(uri+"/api/monitor/get-products"))  # Replace with your actual API endpoint
        response.raise_for_status()  # Check for any HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the server: {e}")
        return []
    
def placeOrder(id, quantity, total_price):
    try:
        requests.post(
                uri+"/api/monitor/place-order",
                headers={
                    'Content-Type':'application/json; charset=UTF-8',
                },
                data=json.dumps({
                    'id': id,
                    'quantity': quantity,
                    'totalPrice': total_price,
                }),
        ) 
        
        # Simulate onSuccess logic
        print("Order placed successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the server: {e}")
        return []
        

# Function to place an order
def place_order():
    selected_drinks = []
    total_price = 0

    for drink in coffee_drinks:
        if drink.var.get() == 1:
            selected_drinks.append(drink.name)
            total_price += drink.price

    if len(selected_drinks) > 0:
        placeOrder(drink.id,1,total_price)
        messagebox.showinfo("Order Placed", f"Your order has been placed! Total price: ${total_price:.2f}")
    else:
        messagebox.showwarning("No Selection", "Please select at least one drink.")


# Function to load image from URL
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((100, 100), Image.ADAPTIVE)
    return ImageTk.PhotoImage(img)

# Function to create drink widgets
async def create_drink_widgets_async():
    loading_label = tk.Label(drinks_frame, text="Loading...")
    loading_label.grid(row=0, column=0)

    product_data = await fetch_coffee_data_async()

    loading_label.destroy()  # Remove loading label once data is fetched

    for i, drink_data in enumerate(product_data):
        image_url = drink_data.get("image_url", "https://res.cloudinary.com/dsx7eoho1/image/upload/v1707628461/Milk/rvqswc9zoaiydspujwvw.jpg")

        drink = Product(
            id = drink_data["_id"],
            name=drink_data["name"],
            description=drink_data["description"],
            price=drink_data["price"],
            image_url=drink_data["image"]
        )

        frame = tk.Frame(drinks_frame, relief=tk.RIDGE, borderwidth=2)
        frame.grid(row=i, column=0, padx=10, pady=10)

        # Load drink image from Cloudinary URL
        drink.tk_image = load_image_from_url(drink.image_url)

        # Create drink image label
        image_label = tk.Label(frame, image=drink.tk_image)
        image_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        # Create drink name label
        name_label = tk.Label(frame, text=drink.name)
        name_label.grid(row=0, column=1, sticky="w")

        # Create drink description label
        description_label = tk.Label(frame, text=drink.description)
        description_label.grid(row=1, column=1, sticky="w")

        # Create drink price label
        price_label = tk.Label(frame, text=f"Price: ${drink.price:.2f}")
        price_label.grid(row=2, column=1, sticky="w")

        # Create drink selection check button
        drink.var = tk.IntVar()
        selection_checkbutton = tk.Checkbutton(frame, variable=drink.var)
        selection_checkbutton.grid(row=0, column=2, rowspan=3)

        coffee_drinks.append(drink)

# Create the main window
window = tk.Tk()
window.title("Coffee Order App")

# Create drinks frame
drinks_frame = tk.Frame(window)
drinks_frame.pack(pady=10)

# Create drink widgets asynchronously
loop = asyncio.get_event_loop()
loop.run_until_complete(create_drink_widgets_async())

# Create place order button
order_button = tk.Button(window, text="Place Order", command=place_order)
order_button.pack(pady=10)

# Run the application
window.mainloop()
