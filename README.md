## PIZZA YETKAZIB BERISH API


## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/jwt/create/``` | _Login user_|_All users_|
| *POST* | ```/auth/jwt/refresh/``` | _Refresh the access token_|_All users_|
| *POST* | ```/auth/jwt/verify/``` | _Verify the validity of a token_|_All users_|
| *POST* | ```/orders/``` | _Place an order_|_All users_|
| *POST* | ```/orders/``` | _Get all orders_|_All users_|
| *GET* | ```/order/{order_id}/``` | _Retrieve an order_|_Superuser_|
| *PUT* | ```/orders/{order_id}/``` | _Update an order_|_All users_|
| *PUT* | ```/update-status/{order_id}/``` | _Update order status_|_Superuser_|
| *DELETE* | ```/delete/{order_id}/``` | _Delete/Remove an order_ |_All users_|
| *GET* | ```/user/{user_id}/orders/``` | _Get user's orders_|_All users_|
| *GET* | ```/user/{user_id}/order/{order_id}/``` | _Get user's specific order_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|

## Project ni ishga tushurish
- Install Postgreql
- Install Python
- Git clone the project with ```---```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Create you database with `python manage.py runserver` 
- Finally run the API 
``` python manage.py runserver ``