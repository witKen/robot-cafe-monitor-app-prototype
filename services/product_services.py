
from asyncore import loop
import requests
from constants.global_variable import *


class ProductServices:
    # Function to fetch coffee drink data from the Node.js server asynchronously
    async def fetch_coffee_data_async():
        try:
            response = await loop.run_in_executor(None, lambda: requests.get(uri+"/api/monitor/get-products"))
            response.raise_for_status()  # Check for any HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from the server: {e}")
            return []