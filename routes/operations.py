from fastapi import APIRouter, HTTPException
from models import Product
from db import Database


router = APIRouter()


DB = Database("products.json")



    
@router.get("/products")
def view_products():
    
    products: dict = DB.read()
    
    if not products:
     raise HTTPException(
            status_code=404,
            detail="No products found"
        )
    else:
        return products

@router.get("/product/{name}")
def get_product_by_name(name:str):
    
    products: dict = DB.read()
    
    if name in products:
        return products
    
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )    
   

@router.post("/product")
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
    

@router.put("/product/{name}")
def sell_product(name:str, quantity:int):
    
    products: dict = DB.read()
    
    if name in products:
        if products[name]["quantity"] >= quantity:
            products[name]["quantity"] -= quantity
            DB.write(products)
            return "Sold successfully"
        return "Quantity insufficient"

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

@router.delete("/product/{name}")
def delete_product(name:str):
    
    products: dict = DB.read()
    
    if name in products:
        del products[name]
        DB.write(products)
        return "Product deleted successfully"
    
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

   