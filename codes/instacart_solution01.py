
"""
Instacart HW InsightData

"""

#%%
import csv
import numpy as np
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
    
    arr = np.zeros((40,3),dtype=int)
    j=40
    for row in orders:
        
        # by inspection we see that there are total of 32974 products
        if  0 < int(row[1]) < 32975 and j>0:
            
            product_id = int(row[1])
            
            dep_id, cart_ords, first_ord = int(row_reader(csv_products,product_id)[3]), int(row[2]), int(row[3])
#            new_row = [int(row_reader(csv_products,product_id)[3]),int(row[2]),int(row[3])]
            print('department_ID=',dep_id)
            arr[40-j] = [dep_id,cart_ords,first_ord] 
            
            #new_row.append(row_reader(csv_products,product_id)[3])
            #print(new_row)
#            ord_dep.writerow(new_row)
            print('j=',40-j)
            j=j-1
arr = arr[arr[:,0].argsort()]      
print(arr)
#with open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\order_products_departments.csv') as csv_ord_dep:
#    new_file = csv.reader(csv_ord_dep) 
#    for row in new_file:
#       
#            print(row)
                    



#%%  first order counter
#def first_ord_counter(arr):
#    counter=0
#    for i in range(0,len(arr[:,0])):
#        
#        if arr[i,2]==0:
#                counter+=1
#    return counter

#%% find the indeces where the deparment_id changes (arr is now sorted according to dep_id)
id0=arr[0,0]
indeces = np.array([0])
for i in range(0,len(arr[:,0])):
        if arr[i,0]==id0:
            print(arr[i,0])
            #id0=arr[i,0]
        else:
            print(arr[i,0])
            indeces=np.append(indeces,i)
            id0=arr[i,0]
      
#%% counting the number of zeros for each department

def first_ord_counter(index,arr): #returns [dep-id, number_of_first_orders]
    
    id0=arr[index,0]
    counter=0
    for i in range(index,len(arr[:,0])):
        if arr[i,0]==id0:
            if arr[i,2]==0:
                counter+=1
            if i==len(arr[:,0])-1:
                return [arr[i,0] , counter]
            #print(arr[i,0])
            #id0=arr[i,0]
        else:
            #print('dep_id=' , arr[i-1,0] , '1st_ord_number=', counter)
            #np.concatenate((first_ord_num,[[ arr[i-1,0] , counter ]]),axis=0)
            return [arr[i-1,0] , counter]
 
#%% build the array of number of 1st orders from each department    'dep_id','number_of_1st_ords'
first_ord_num = np.array([first_ord_counter(0,arr)])

for index in indeces[1:]:
    first_ord_num = np.concatenate(( first_ord_num, [first_ord_counter(index,arr)]), axis=0 )
                         
