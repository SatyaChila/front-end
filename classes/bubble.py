list = list(map(int,input("Enter the list").split()))
len = len(list)
for i in range(0,len-1):
    for j in range(i+1,len):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)