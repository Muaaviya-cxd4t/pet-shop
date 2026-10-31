import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "replace-this-secret-before-deployment")

PRODUCTS = [
    {"id": 1, "name": "The Daily Crunch", "category": "Food", "type": "Dog food", "price": 899, "tag": "BESTSELLER", "description": "Complete chicken & rice kibble for happy everyday zoomies.", "image": "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=900&q=85"},
    {"id": 2, "name": "Salmon Supper", "category": "Food", "type": "Cat food", "price": 549, "tag": "GRAIN FREE", "description": "Tasty salmon bites made for your tiny kitchen supervisor.", "image": "https://images.unsplash.com/photo-1582798358481-d199fb7347bb?auto=format&fit=crop&w=900&q=85"},
    {"id": 3, "name": "Peanut Butter Bites", "category": "Treats", "type": "Dog treats", "price": 249, "tag": "GOOD DOG ENERGY", "description": "Crunchy little rewards for very good behaviour. Mostly.", "image": "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=900&q=85"},
    {"id": 4, "name": "The Big Squeak", "category": "Toys", "type": "Dog toy", "price": 399, "tag": "PLAYTIME", "description": "A squeaky pal for serious tug-of-war professionals.", "image": "https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=900&q=85"},
    {"id": 5, "name": "Feather Frenzy", "category": "Toys", "type": "Cat toy", "price": 199, "tag": "CAT APPROVED", "description": "Wiggles, flutters and suspiciously intense pouncing.", "image": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=900&q=85"},
    {"id": 6, "name": "Cloud Nine Bed", "category": "Accessories", "type": "Pet bed", "price": 1299, "tag": "NAP MATERIAL", "description": "A soft landing spot for post-adventure power naps.", "image": "https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?auto=format&fit=crop&w=900&q=85"},
    {"id": 7, "name": "Walkies Kit", "category": "Accessories", "type": "Leash set", "price": 699, "tag": "READY TO GO", "description": "A comfy leash and collar set for neighbourhood patrols.", "image": "https://images.unsplash.com/photo-1551717743-49959800b1f6?auto=format&fit=crop&w=900&q=85"},
    {"id": 8, "name": "Tuna Temptations", "category": "Treats", "type": "Cat treats", "price": 229, "tag": "TINY TREAT", "description": "Little fishy treats for the household's actual boss.", "image": "https://images.unsplash.com/photo-1573865526739-10659fec78a5?auto=format&fit=crop&w=900&q=85"},
]

def get_cart():
    cart = session.get("cart", {})
    items, subtotal = [], 0
    for product in PRODUCTS:
        qty = int(cart.get(str(product["id"]), 0))
        if qty > 0:
            line_total = product["price"] * qty
            items.append({**product, "quantity": qty, "line_total": line_total})
            subtotal += line_total
    return items, subtotal

@app.route("/")
def home():
    items, subtotal = get_cart()
    count = sum(item["quantity"] for item in items)
    return render_template("index.html", products=PRODUCTS, cart_items=items,
                           subtotal=subtotal, cart_count=count)

@app.post("/add/<int:product_id>")
def add(product_id):
    if not any(p["id"] == product_id for p in PRODUCTS):
        flash("That product could not be found.", "error")
        return redirect(url_for("home"))
    cart = session.get("cart", {})
    key = str(product_id)
    cart[key] = min(int(cart.get(key, 0)) + 1, 20)
    session["cart"] = cart
    flash("Added to your pet's goodie pile!", "success")
    return redirect(url_for("home") + "#shop")

@app.post("/cart/update/<int:product_id>")
def update_cart(product_id):
    cart = session.get("cart", {})
    key = str(product_id)
    try:
        qty = int(request.form.get("quantity", 0))
    except ValueError:
        qty = 0
    if qty <= 0:
        cart.pop(key, None)
    else:
        cart[key] = min(qty, 20)
    session["cart"] = cart
    return redirect(url_for("home") + "#cart")

@app.post("/checkout")
def checkout():
    items, subtotal = get_cart()
    if not items:
        flash("Your cart needs at least one tail-wagging item.", "error")
        return redirect(url_for("home") + "#shop")
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()
    if not all([name, phone, address]):
        flash("Please complete all delivery details.", "error")
        return redirect(url_for("home") + "#cart")
    order_id = "GB" + datetime.now().strftime("%y%m%d%H%M%S")
    session["cart"] = {}
    return render_template("success.html", name=name, order_id=order_id, total=subtotal)

if __name__ == "__main__":
    app.run(debug=True)
