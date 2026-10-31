# Good Boy Pet Supply Club

A responsive pet food, treats, toys and accessories storefront built with Flask.

## Features
- Responsive storefront with pet-shop branding
- Product categories and filters
- Eight sample products with INR pricing
- Session-based shopping bag
- Update quantities and remove products
- Demo checkout and order confirmation
- Mobile-friendly layout

## Run locally

1. Open this folder in VS Code.
2. (Recommended) Create a virtual environment:

   ```bash
   py -m venv venv
   venv\Scripts\activate
   ```

   On macOS/Linux use `python3 -m venv venv` and `source venv/bin/activate`.

3. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Flask:

   ```bash
   python app.py
   ```

5. Visit http://127.0.0.1:5000

## Deploy
Use `gunicorn app:app` as the start command on a compatible Flask host.
Set a strong `SECRET_KEY` environment variable and do not run Flask debug mode in production.

## Demo limitations
Checkout only displays a confirmation page. It does not collect payment, persist orders to a database, or create real deliveries. Product photos are externally hosted and require an internet connection.
