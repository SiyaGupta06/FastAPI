import os
import json

from models import Product
 

class Database:
    def __init__(self, file_path:str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump({}, f)
    
    def read(self) -> Product:
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data
    
    def write(self, products:Product):
        with open(self.file_path, 'w') as f:
            data = json.dump(products, f, indent=4)
            print(data)