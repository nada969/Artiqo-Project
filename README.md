
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
🌟 Project Name:
Artiqo – The Artsy Marketplace for Local Legends

📌 What’s This All About?
Artiqo is your go-to online marketplace that connects local artists (aka creative geniuses) with awesome buyers who love unique, handmade goods. 🎁 Whether you're here to sell your soul on canvas or snag some rare art for your wall, Artiqo makes it smooth with features like secure logins, organized product listings, a chill cart system, and safe payments. 🎨🛒💳

✨ What Makes Artiqo Shine?
- User Roles – Artists do the uploading, buyers do the buying. Everyone wins!
- Product Listings – Artists can add, tweak, or remove their masterpieces.
- Cart System – Add it, update it, buy it—your cart, your rules.
- Order Management – Keep tabs on your past and present purchases.
- Payments – Smooth, secure, and with status updates so you know what’s up.
- Artist Profiles – Each artist gets their own artsy corner of the platform to flex their skills and tell their story.

🛠️ Tech Behind the Magic
- Backend: Python (Django – solid, like your favorite sketchbook)
- Database: MySQL (storing art data like it’s the Louvre)
- Authentication: JWT (for login that doesn’t mess around)

📡 API Endpoints :

- Users :
          - /users/viewUsers , Get, View users
          - /users/register	,POST,	Register a new user
          - /users/login	,POST,	Log in and get that sweet access
            
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
          
- Admin:
          -  /admin/          ,Get,   to vieww the admin page



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


✅ Frontend: React.js

✅  API Endpoints :
- Users :
          - /users/{userId}/profile	,GET,	View a user's profile
          - /users/{userId}/profile	,PUT,	Update user profile
- Products:	
          /products	,GET,	View all products
          /products	,POST,	Artists can add a new product
          /products/{productId}	,PUT,	Update product details
          /products/{productId}/remove	,DELETE,	Delete a product
-Orders:
          /orders/{userId}	,GET,	View all orders by the user
          /orders/{orderId}	,GET,	View a specific order
          /orders/{userId}/add	,POST,	Create a new order
          /orders/{userId}/cancel	,PUT,	Cancel an order (status update)
- Payments	
          /payment/{paymentId}	,POST,	Make a payment


