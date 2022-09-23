n=int(input("How many Items? "))
w=int(input("Total Capacity: "))
print("Enter items Weight And Value In Separate Lines ")
items=[]
for i in range(n):
    weight,value=map(int,input("items %d: " %(i+1)).split())
    items.append([weight,value,value/weight])
sorted_items=sorted(items,key=lambda x:x[2],reverse = True)
profit=0
W=w
for i in range(n):
    if W>=sorted_items[i][0]: 
          profit+=sorted_items[i][1]
          W-=sorted_items[i][0]
    else:
       profit+=(sorted_items[i][2]*w)
       break
print("Sorted_items for Per Unit value disingding order:",sorted_items)
print("Total Profit Is: %d"%profit)
