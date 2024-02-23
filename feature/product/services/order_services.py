import json
from tkinter import messagebox
import requests
from constants.global_variable import *

class OrderServices:
    def placeOrder(id, quantity, total_price):
        try:
            response = requests.post(
                uri + "/api/monitor/place-order",
                headers={
                    'Content-Type': 'application/json; charset=UTF-8',
                },
                data=json.dumps({
                    'id': id,
                    'quantity': quantity,
                    'totalPrice': total_price,
                }),
            )
            
            # Check if the request was successful (status code 2xx)
            if response.status_code // 100 == 2:
                # Simulate onSuccess logic
                messagebox.showinfo("Order Placed", f"Your order has been placed! Total price: ${total_price:.2f}")
            else:
                # Handle non-successful status codes
                messagebox.showerror("Order Placement Failed", f"Failed to place order. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            messagebox.showerror("Error", f"Error: {e}")
            return []
