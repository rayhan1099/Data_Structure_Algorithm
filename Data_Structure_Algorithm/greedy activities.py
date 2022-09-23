s=input("Enter Starting Times: ").split()
s=[int(i) for i in s]
f=input("Enter Ending Times: ").split()
f=[int(i) for i in f]
n=len(s)
a=[0]
i = 0
for m in range (1,n):

  if s[m]>=f[i]:

    a.append(m)
    i = m
print("Selected Activites: ",end=' ')
print(a)

for element in a:
  print(f[element],end=' ')