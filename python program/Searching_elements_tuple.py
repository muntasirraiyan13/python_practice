x=int(input("Enter the number:"))
numbers=(1,4,9,16,25,36,49,64,81,100)
count=0
while count<len(numbers):
    if(numbers[count]==x):
        print("Found at index",count)
        break
    count=count+1
else:
    print("Not found")
