
"""
Instacart HW InsightData

"""
#%%
import csv
import numpy as np

#%%
j=10
with open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\products.csv') as prodcsv:
    products = csv.reader(prodcsv, delimiter=',')
    for row in products:
        if j>0:
            print(row)
            j=j-1
        else:
            break
    

#%% define a row reader (row_asked=0 is the first row which is the header)
def row_reader(csv_file,row_asked):
    csv_file.seek(0)
    for index, row in enumerate(csv.reader(csv_file)):
        if index == row_asked:
            return row
        
        
#%%  

with open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\order_products_departments.csv', "w", newline='') as csv_ord_dep,\
     open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\products.csv') as csv_products,\
     open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\order_products__train.csv') as csv_orders:
         
    orders = csv.reader(csv_orders, delimiter=',')
    products = csv.reader(csv_products, delimiter=',' )
    ord_dep = csv.writer(csv_ord_dep)
# 
    
    
    
    ord_dep.writerow(['department_id', 'add_to_cart_orders', 'number_of_first_orders', 'percentage']) 


    next(orders,None)   # skip the header
    
    arr = np.empty((20,3))
    j=20
    for row in orders:
        
        # by inspection we see that there are total of 32974 products
        if  0 < int(row[1]) < 32975 and j>0:
            
            product_id = int(row[1])
            print(product_id)
            dep_id, cart_ords, first_ord = int(row_reader(csv_products,product_id)[3]), int(row[2]), int(row[3])
#            new_row = [int(row_reader(csv_products,product_id)[3]),int(row[2]),int(row[3])]
            arr[20-j] = [dep_id,cart_ords,first_ord] 
            arr = arr[arr[:,0].argsort()]
            #new_row.append(row_reader(csv_products,product_id)[3])
            #print(new_row)
#            ord_dep.writerow(new_row)
            j=j-1
            
print(arr)
#with open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\order_products_departments.csv') as csv_ord_dep:
#    new_file = csv.reader(csv_ord_dep) 
#    for row in new_file:
#       
#            print(row)
                    



#%%  first order counter
def first_ord_counter(arr):
    counter=0
    for i in range(0,len(arr[:,0])):
        
        if arr[i,2]==0:
                counter+=1
    return counter
      
#%% counting the number of zeros for each department
def count(index,arr):
    id0=arr[index,0]
    counter=0
    for i in range(index,len(arr[:,0])):
        if arr[i,0]==id0:
            if arr[i,2]==0:
                counter+=1
            print(arr[i,0])
            id0=arr[i,0]
        else:
            return print(i,counter)
            break              
