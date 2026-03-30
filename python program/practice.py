word=""
for i in range(4):
    letter=input("Enter a letter:")
    word=word+letter
print("Word:",word)
if (word.endswith("s")):
    print("YES")
else:
    print("NO")

