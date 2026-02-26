x=int(input("Enter a number to run your loop:"))
count=1
while count<=x:
    if(count%2==0):
        count=count+1
        continue
    print(count)
    count=count+1
