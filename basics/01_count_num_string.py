print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord('0'))
print(ord('9'))
ass=65
print(chr(ass))

#--------------------------------------------------------
s="sumITG@#upta25411"
lower_case=0
upper_case=0
numeric=0
special=0
for i in s:
    if ord(i) >=65 and ord(i) <=90:
        upper_case+=1
    if ord(i) >=90 and ord(i) <=122:
        lower_case+=1
    else:
        numeric+=1
print(f"tottal lower_case is {lower_case} and upper_case is {upper_case} and numeric is {numeric}")        

