
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
  
****GET****                                    https://Artiqo.com/api/v1/product/products

Retrieve all Products

 Response:
      
      - 200: OK
      - 404: Not Found
      - 500: Internal Server Error

- Orders:
  
****GET****                                    https://Artiqo.com/api/v1/order/orderartview

Retrieve all Special Art Orders 

 Response:

      - 200: OK
      - 404: Not Found
      - 500: Internal Server Error
---
**Implementing Authorization :**

Artist:

- upload his art
- edit item details
- delete item
- show the ordered item from his arts
- accept the special order or not

Client:

- Browse products
- place order from existing items
- place special order
- browse own orders
- Add to cart
- Review items
---
DataBase Design:
![image](https://github.com/user-attachments/assets/671277ee-9210-40d1-99c8-c1235dbfd379)
