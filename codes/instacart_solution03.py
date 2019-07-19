
"""
Instacart HW InsightData

"""
#%% import the modules
import csv
import numpy as np

#%%  inspect the data 
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

with open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\products.csv', encoding='utf8') as csv_products,\
     open('E:\Saeed\Data Science\Instacart\instacart_2017_05_01\order_products__train.csv') as csv_orders:
         
    orders = csv.reader(csv_orders, delimiter=',')
    products = csv.reader(csv_products, delimiter=',' )
    
#     
    ord_dep.writerow(['department_id', 'add_to_cart_orders', 'number_of_first_orders', 'percentage']) 


    next(orders,None)   # skip the header
    
    #num_orders = 1384617
    num_orders = 10000
    
    # determine how many orders to read
    j= num_orders
    arr = np.zeros((num_orders,3),dtype=int)
    for row in orders:
        
            # products.csv is sorted according to the product_id
            
            product_id = int(row[1])   
            dep_id, cart_ords, first_ord = int(row_reader(csv_products,product_id)[3]), int(row[2]), int(row[3])
            
            print(j)    #see the progress of reading the data
            
            if cart_ords > 0:
                arr[num_orders-j] = [dep_id,cart_ords,first_ord] 
            
            j=j-1  
                 
csv_ord_dep.close()
csv_products.close()

#%% sort the array according to depatment number; arr = [dep_id, cart_ords, first_ord]
arr_sort = arr[arr[:,0].argsort()]      
print(arr_sort)


#%% find the indeces where the deparment_id changes (arr is now sorted according to dep_id)
### ( arr = [dep_id, cart_ords, first_ord])
def dep_change_index(arr):
    id0=arr[0,0]
    indeces = np.array([0])
    for i in range(0,len(arr[:,0])):
        if arr[i,0] != id0:
            
            indeces=np.append(indeces,i)
            id0=arr[i,0]
    return indeces      
#%% counting the number of orders and number of first reorders for each department
### ( arr = [dep_id, cart_ords, first_ord] )
def order_counter(index,arr): #returns [dep-id, number_of_orders, number_of_first_orders, percentage]
    
    id0=arr[index,0]
    count_first_ord = 0
    count_ord = 0
    for i in range(index,len(arr[:,0])):
        if arr[i,0]==id0:
            count_ord+=1
            if arr[i,2]==0:
                count_first_ord+=1
            if i==len(arr[:,0])-1:
                return [int(arr[i,0]) , int(count_ord) ,int(count_first_ord), round(count_first_ord/count_ord,2)]
            #print(arr[i,0])
            #id0=arr[i,0]
        else:
            #print('dep_id=' , arr[i-1,0] , '1st_ord_number=', counter)
            #np.concatenate((first_ord_num,[[ arr[i-1,0] , counter ]]),axis=0)
            return [int(arr[i-1,0]) ,int(count_ord), int(count_first_ord), round(count_first_ord/count_ord,2)]

 
#%% build the final array ( 'dep_id', 'number_of_ords','number_of_1st_ords','percentage')
final_list = np.array([['department_id', 'number_of_orders','number_of_first_orders','percentage']])

for index in dep_change_index(arr_sort):
    final_list = np.concatenate(( final_list, [order_counter(index,arr_sort)]), axis=0 )
         
#%% write to the output report.csv                
    
with open('E:\\Saeed\\Data Science\\Instacart\\instacart_2017_05_01\\report.csv', "w", newline='') as csv_report:
    
    rep = csv.writer(csv_report)
    
    
    for i in range(len(final_list)):
        rep.writerow(final_list[i])
        
    
     
