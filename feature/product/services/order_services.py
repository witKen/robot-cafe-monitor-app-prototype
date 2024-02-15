import json
import requests
from constants.global_variable import *


class OrderServices:
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