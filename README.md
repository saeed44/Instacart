
Instacart

First I read the lines in the  'order_products_train.csv' file. By matching the "product_id"s in the 'products.csv' file with the ones in 'order_products_train.csv', add the correct "department_id" to the orders data. Then I add the lines as numpy arrays to "arr" in the the form  "[department_id, cart_ords, first_ord]". This is the main time consuming part as there are ~1,300,000 lines to read from 'order_products_train.csv'. 
Once we build the numpy array "arr", the rest of the code just sorts the array according to the "department_id" and counts the number of orders, the number of first orders and their fraction, and add each department statistics to the array "final_list".
 
Finally we write the lines in "fianl_list" in the 'report.csv' file.

Some notes:

    In builing the main numpy array, we ignore the products that have not been ordered.
 
