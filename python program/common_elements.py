list1=[1,3,5,2,6,8,9,-2]
list2=[0,-2,3,6,9,-5,1,10]
common_elements=[]
for i in list1:
    if i in list2:
        common_elements.append(i)
print(common_elements)
