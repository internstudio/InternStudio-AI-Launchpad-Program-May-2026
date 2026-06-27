/*====================================================
        E-COMMERCE MANAGEMENT SYSTEM
====================================================*/


/*====================================================
                CREATE DATABASE
====================================================*/

DROP DATABASE IF EXISTS ecommerce_system;

CREATE DATABASE ecommerce_system;

USE ecommerce_system;


/*====================================================
                CUSTOMERS TABLE
====================================================*/

CREATE TABLE Customers(

customer_id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) NOT NULL,

email VARCHAR(100) UNIQUE NOT NULL,

phone VARCHAR(15),

address TEXT,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



/*====================================================
                CATEGORIES TABLE
====================================================*/

CREATE TABLE Categories(

category_id INT AUTO_INCREMENT PRIMARY KEY,

category_name VARCHAR(100) UNIQUE NOT NULL

);



/*====================================================
                PRODUCTS TABLE
====================================================*/

CREATE TABLE Products(

product_id INT AUTO_INCREMENT PRIMARY KEY,

product_name VARCHAR(150) NOT NULL,

description TEXT,

price DECIMAL(10,2) NOT NULL,

stock_quantity INT DEFAULT 0,

category_id INT,

FOREIGN KEY(category_id)

REFERENCES Categories(category_id)

);



/*====================================================
                CART TABLE
====================================================*/

CREATE TABLE Cart(

cart_id INT AUTO_INCREMENT PRIMARY KEY,

customer_id INT,

product_id INT,

quantity INT DEFAULT 1,

FOREIGN KEY(customer_id)

REFERENCES Customers(customer_id),

FOREIGN KEY(product_id)

REFERENCES Products(product_id)

);



/*====================================================
                ORDERS TABLE
====================================================*/

CREATE TABLE Orders(

order_id INT AUTO_INCREMENT PRIMARY KEY,

customer_id INT,

order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

status VARCHAR(50)

DEFAULT 'Pending',

FOREIGN KEY(customer_id)

REFERENCES Customers(customer_id)

);



/*====================================================
            ORDER ITEMS TABLE
====================================================*/

CREATE TABLE Order_Items(

order_item_id INT AUTO_INCREMENT PRIMARY KEY,

order_id INT,

product_id INT,

quantity INT,

price DECIMAL(10,2),

FOREIGN KEY(order_id)

REFERENCES Orders(order_id),

FOREIGN KEY(product_id)

REFERENCES Products(product_id)

);



/*====================================================
                PAYMENTS TABLE
====================================================*/

CREATE TABLE Payments(

payment_id INT AUTO_INCREMENT PRIMARY KEY,

order_id INT UNIQUE,

payment_method VARCHAR(50),

amount DECIMAL(10,2),

payment_status VARCHAR(30),

payment_date TIMESTAMP

DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY(order_id)

REFERENCES Orders(order_id)

);



/*====================================================
                REVIEWS TABLE
====================================================*/

CREATE TABLE Reviews(

review_id INT AUTO_INCREMENT PRIMARY KEY,

customer_id INT,

product_id INT,

rating INT CHECK(rating BETWEEN 1 AND 5),

comment TEXT,

FOREIGN KEY(customer_id)

REFERENCES Customers(customer_id),

FOREIGN KEY(product_id)

REFERENCES Products(product_id)

);



/*====================================================
            INSERT CATEGORIES
====================================================*/

INSERT INTO Categories(category_name)

VALUES

('Electronics'),

('Fashion'),

('Books'),

('Home Appliances'),

('Sports');



/*====================================================
            INSERT CUSTOMERS
====================================================*/

INSERT INTO Customers(

name,

email,

phone,

address

)

VALUES


('John Doe',

'john@gmail.com',

'9876543210',

'New York'),


('Jane Smith',

'jane@gmail.com',

'9988776655',

'California'),


('Michael Brown',

'michael@gmail.com',

'9123456789',

'Texas');




/*====================================================
            INSERT PRODUCTS
====================================================*/

INSERT INTO Products(

product_name,

description,

price,

stock_quantity,

category_id

)

VALUES


('Laptop',

'Gaming Laptop',

75000,

15,

1),


('T-Shirt',

'Cotton T-Shirt',

800,

50,

2),


('SQL Book',

'Database Learning Book',

650,

25,

3),


('Microwave Oven',

'25L Microwave',

12000,

10,

4),


('Football',

'Leather Football',

1500,

30,

5);




/*====================================================
            INSERT CART ITEMS
====================================================*/

INSERT INTO Cart(

customer_id,

product_id,

quantity

)

VALUES


(1,1,2),

(1,2,1),

(2,5,1);



/*====================================================
            CREATE ORDERS
====================================================*/

INSERT INTO Orders(customer_id)

VALUES

(1),

(2);




/*====================================================
            INSERT ORDER ITEMS
====================================================*/

INSERT INTO Order_Items(

order_id,

product_id,

quantity,

price

)

VALUES


(1,1,2,75000),

(1,2,1,800),

(2,5,1,1500);




/*====================================================
            INSERT PAYMENTS
====================================================*/

INSERT INTO Payments(

order_id,

payment_method,

amount,

payment_status

)

VALUES


(1,

'UPI',

150800,

'Completed'),


(2,

'Credit Card',

1500,

'Completed');




/*====================================================
            INSERT REVIEWS
====================================================*/

INSERT INTO Reviews(

customer_id,

product_id,

rating,

comment

)

VALUES


(1,

1,

5,

'Excellent Laptop'),


(2,

5,

4,

'Good quality football');



/*====================================================
            UPDATE PRODUCT STOCK
====================================================*/

UPDATE Products

SET stock_quantity = stock_quantity - 2

WHERE product_id = 1;



UPDATE Products

SET stock_quantity = stock_quantity - 1

WHERE product_id = 5;



/*====================================================
            DELETE CART ITEMS
====================================================*/

DELETE FROM Cart

WHERE customer_id = 1;



/*====================================================
                CREATE INDEXES
====================================================*/

CREATE INDEX idx_product_name

ON Products(product_name);



CREATE INDEX idx_customer_email

ON Customers(email);



/*====================================================
            DISPLAY ALL CUSTOMERS
====================================================*/

SELECT *

FROM Customers;



/*====================================================
            DISPLAY ALL PRODUCTS
====================================================*/

SELECT *

FROM Products;



/*====================================================
            DISPLAY CATEGORIES
====================================================*/

SELECT *

FROM Categories;



/*====================================================
        PRODUCTS WITH CATEGORY NAME
====================================================*/

SELECT


Products.product_name,

Categories.category_name


FROM Products


JOIN Categories


ON Products.category_id

=

Categories.category_id;



/*====================================================
            CUSTOMER CART DETAILS
====================================================*/

SELECT


Customers.name,


Products.product_name,


Cart.quantity,


Products.price,


(Cart.quantity *

Products.price)

AS Total


FROM Cart


JOIN Customers


ON Customers.customer_id

=

Cart.customer_id



JOIN Products


ON Products.product_id

=

Cart.product_id;




/*====================================================
            CUSTOMER ORDER HISTORY
====================================================*/

SELECT


Customers.name,


Orders.order_id,


Orders.status,


Orders.order_date


FROM Orders


JOIN Customers


ON Customers.customer_id

=

Orders.customer_id;




/*====================================================
            COMPLETE ORDER DETAILS
====================================================*/

SELECT


Orders.order_id,


Customers.name,


Products.product_name,


Order_Items.quantity,


Order_Items.price,


(Order_Items.quantity *

Order_Items.price)

AS Amount


FROM Order_Items


JOIN Orders


ON Orders.order_id

=

Order_Items.order_id



JOIN Customers


ON Customers.customer_id

=

Orders.customer_id



JOIN Products


ON Products.product_id

=

Order_Items.product_id;




/*====================================================
                PRODUCT REVIEWS
====================================================*/

SELECT


Customers.name,


Products.product_name,


Reviews.rating,


Reviews.comment


FROM Reviews


JOIN Customers


ON Customers.customer_id

=

Reviews.customer_id



JOIN Products


ON Products.product_id

=

Reviews.product_id;




/*====================================================
                TOP SELLING PRODUCTS
====================================================*/

SELECT


Products.product_name,


SUM(Order_Items.quantity)

AS TotalSold


FROM Order_Items


JOIN Products


ON Products.product_id

=

Order_Items.product_id


GROUP BY product_name


ORDER BY TotalSold DESC;




/*====================================================
            TOTAL SALES AMOUNT
====================================================*/

SELECT


SUM(quantity * price)

AS GrandTotal


FROM Order_Items;




/*====================================================
                TRANSACTION DEMO
====================================================*/

START TRANSACTION;


INSERT INTO Orders(customer_id)

VALUES(3);


INSERT INTO Payments(

order_id,

payment_method,

amount,

payment_status

)

VALUES(

3,

'Debit Card',

650,

'Completed'

);


COMMIT;


/*====================================================
                ROLLBACK DEMO
====================================================*/

-- ROLLBACK;



/*====================================================
                END OF FILE
====================================================*/