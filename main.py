from fastapi import FastAPI
from models import Product
from db import Database


app = FastAPI()


DB = Database("products.json")

    
@app.get("/products")
def view_products():
    
    products: dict = DB.read()
    
    if not products:
     return"No products found"
        
    else:
        return products

@app.get("/product/{name}")
def get_product_by_name(name:str):
    
    products: dict = DB.read()
    
    if name in products:
        return products[name]
    
    else:
     return"Product not found"
    
   

@app.post("/product")
def add_product(product:Product):
    
    products: dict = DB.read()
   
    if product.name in products:
            return "Product already exists"
    else:
        products[product.name] = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        }
        DB.write(products)
        return "Product added successfully"
    

@app.put("/product/{name}")
def sell_product(name:str, quantity:int):
    
    products: dict = DB.read()
    
    if name in products:
        if products[name]["quantity"] >= quantity:
            products[name]["quantity"] -= quantity
            DB.write(products)
            return "Sold successfully"
        return "Quantity insufficient"
    else:
     return"Product not found"

@app.delete("/product/{name}")
def delete_product(name:str):
    
    products: dict = DB.read()
    
    if name in products:
        del products[name]
        DB.write(products)
        return "Product deleted successfully"
    else:
     return"Product not found"
    




