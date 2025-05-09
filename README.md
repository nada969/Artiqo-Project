
**# 1- Introduction**

**## Objectives**

- Artists can showcase their arts, each art has its unique vibe.
- Buyers can see the arts, and order.
- Buyer can order his special order, and the artist will receive a mail of this order.
- Admin can monetize the platform through transaction fees, subscriptions, or featured listings

**## Scope**

Build an online marketplace where local artists can showcase and sell their drawings. This platform will connect artists with buyers.

**## Stakeholders**

- Artist want to showcase their arts.
- Buyers want to find their special test of art.

**# 2- Functional Requirements**

- Buyer can create his profile.
- Buyer can see the arts categorized by their artist.
- Buyer can order his own art.
- Buyer can search for an art.
- recommended relevant arts for user based on his order.
- Buyer complete his payment
- Artist see the orders from his arts.
- Artist receive the special art ordered via mail.
- Artist can upload the new art.

**# 3- Data Requirements**

- Users
- Products
- Orders
- Carts
- Payments

**# 4- Tools and Technologies**

- Django /python

- MySQL Data Base
- **REST API/** postman

---

**API Design:**

- Users :
****GET****                                    https://Artiqo.com/api/v1/users/viewUsers

Retrieve all users

 Response:

- 200: OK
- 404: Not Found
- 500: Internal Server Error

****POST****                                    https://Artiqo.com/api/v1/users/register

Request:

```json
{
    "username": "username",
    "email": "email",
    "password": "password"
}
```

 Response:

- 201: User Created
- 400: Bad Request
- 405: method not allowed (if I choose invalid HTTP method)
- 500: Internal Server Error

****POST****                                    https://Artiqo.com/api/v1/users/login

Request:

```json
{
    "username": "username",
    "password": "password"
}
```

 Response:

- 201: User login
- 400: Bad Request
- 401: Unauthorized (username and password don’t match)
- 405: method not allowed (if I choose invalid HTTP method)
- 500: Internal Server Error
            
- Products:	
          - /products/{productId}	,GET,	View a single product
          - /products/products     , Get, view all products
- Cart:	
          - /cart/{userId}	,GET,	View the user’s cart
          - /cart/{userId}/add	,POST,	Add a product to the cart
          - /cart/{userId}/update	,PUT,	Update product quantity
          - /cart/{userId}/remove/{productId}	,DELETE,	Remove a product from the cart
- Orders:
          - /order/orderartview/ Get,     to view the orders
           

Next Steps:

✅ Implement the order workflow:
Users place an order via neworder.html.
Send order requests to the artist via email.
✅ Implement the cart functionality:
If the user is logged in, items are added to the cart.
If the user is not logged in, redirect them to login.html.
✅ Implement user authentication features:
Logout functionality
Profile management (profile.html)
Cart view (cart.html)
✅ Payment System:
Secure payments with idempotency to avoid double charges or chaos. source  
Payment status updates included: pending, completed, failed.


