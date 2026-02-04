# Aforro-Backend-Assignment
This is a Django backend project scaffold for the Aforro Backend Developer assignment.
The project is a backend-only application built using Django and Django REST Framework, focusing on order management, inventory handling, product search, and scalability.
git clone https://github.com/Vaishnavijingar/Aforro-Backend-Assignment.git
cd aforro-backend-assignment

Run the Application Using Docker
Make sure Docker and Docker Compose are installed.
docker-compose up --build

Backend API will be available at:
http://localhost:8000

Run Database Migrations
docker-compose exec web python manage.py seed_data


API Details
🔹 Create Order
POST /orders/
Request 


Body
{
  "store_id": 1,
  "items": [
    { "product_id": 10, "quantity_requested": 2 },
    { "product_id": 15, "quantity_requested": 1 }
  ]
}




Response



{
  "status": "CONFIRMED",
  "order_id": 5
}




🔹 List Orders for a Store
GET /stores/<store_id>/orders/
Response

[
  {
    "order_id": 5,
    "status": "CONFIRMED",
    "created_at": "2026-02-04T10:15:00Z",
    "total_items": 3
  }
]

🔹 Store Inventory
GET /stores/<store_id>/inventory/
Response
[
  {
    "product_title": "Laptop",
    "price": 55000,
    "category": "Electronics",
    "quantity": 12
  }
]

🔹 Product Search
GET /api/search/products/

🔹 Autocomplete API

GET /api/search/suggest/?q=lap

Rules
Minimum 3 characters required
Maximum 10 results
Prefix matches prioritized

🧠 Assumptions and Design Decisions

1. This is a backend-only service (no frontend UI).
2. Order creation is wrapped in transaction.atomic() to ensure data consistency.
3. select_for_update() is used to prevent race conditions during inventory updates.
4. Redis is used for caching to improve API performance.
5. Celery is used for asynchronous background tasks.
6. icontains search is used instead of full-text search for simplicity.
7. Docker is used for consistent setup across environments.
