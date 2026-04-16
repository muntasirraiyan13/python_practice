arr=[1,8,9,5,6,3]
target=int(input("Enter the number:"))
for i in range(len(arr)):
    if (arr[i]==target):
        print("The number is found at index,",i)
        break
    
        
