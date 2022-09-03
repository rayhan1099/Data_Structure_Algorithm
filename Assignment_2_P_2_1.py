activities=[[5,9],[12,15],[5,6],[11,12],[3,11],[8,14],[11,13]]
n=len(activities)
print("Given Activities For ID-200101099:\n",activities)
print("Number Of Activities:",n)
sorted_item = sorted(activities,key=lambda x:x[1]-x[0])
print("Sorted The Following Activities Is:\n",sorted_item)
a=[0]
i=0
for r in range(1,n):
    if sorted_item[r][0]>=sorted_item[i][1]:
         a.append(r)
         i=r
print("Selected Activites For Shortest Interval Time: ",end=' ')
for element in a:
          print(sorted_item[element],end=' ')
print("\nSelected Index For Shortest Interval Time:",a)

   