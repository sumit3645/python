number=[14,2,145,65,987,4,6]

ans=float('-inf')    #lower number is - infinity then compare
for num in number:
    if num > ans:
        ans=num
    else:
        continue
print(ans)    
