a=[1,2,6,7,3,4]
max1=a[0]
for i in range(len(a)):
    if(a[i]>max1):
        max1=a[i]
print(max1)
max2=0
for i in range(len(a)):
    if a[i]!= max1:
        if max2 is 0 or a[i]>max2:
            max2 = a[i]
print("second max",max2)            
