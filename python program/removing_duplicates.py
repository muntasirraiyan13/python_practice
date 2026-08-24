list=[1,2,3,2,9,8,1,3,9]
unique=[]
for i in list:
    if i not in unique:
        unique.append(i)
print(unique)
