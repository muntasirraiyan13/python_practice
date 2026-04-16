arr=[1,3,5,7,9,11]
target=int(input("Enter the number:"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if (arr[mid]==target):
        print("The number is found at index,",mid)
        break
    elif (arr[mid]<target):
        low=mid+1
    elif(arr[mid]>target):
        high=mid-1
