n=int(input("How Many Activities? "))
print("Enter activities Starting and End Time in Separate Lines.")
activities=[]
for i in range(n):
    s,f=map(int,input("Activity %d: "% (i+1)).split())
    activities.append([s,f])
sorted_item = sorted(activities)
print(sorted_item)
a=[0]
i=0
for m in range(1,n):
    if sorted_item[m][0]>=sorted_item[i][1]:
         a.append(m)
         i=m
print("Selected Activites: ",end=' ')
for element in a:
          print(sorted_item[element],end=' ')
print("\nSelected Index:",a)

