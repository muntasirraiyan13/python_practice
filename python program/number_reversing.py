n=int(input("How many times?:"))
for _ in range(n):
    N = int(input("Enter a number which will be reversed:"))
    s = str(N)
    reversed_s = s[::-1]
    reversed_N = int(reversed_s)
    print(reversed_N)
