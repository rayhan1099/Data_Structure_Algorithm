n=int(input("Enter How many elements?"))
w=int(input("Enter Total capacity "))
print("enter Weight and value in seaprate line ")
items=[]
for i in range(n):
    weight,value=map(int,input("items %d:"%(i+1)).split())
    items.append([weight,value,value/weight])
    sorted_items=sorted(items,key=lambda x:x[2],reverse=True)
profit=0
for i in range(n):
    if w>=sorted_items[i][0]:
        profit+=sorted_items[i][1]
        w-=sorted_items[i][0]
    else:
        profit=sorted_items[i][2]*w
        break
print("sorted in per unit desingding order",sorted_items)
print("total profit %d"%profit)