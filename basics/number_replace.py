n=1004
strn=str(n)
res=''
for i  in strn:
    if i =='0':
        res=res + '5'
    else:
        res=res + i
print(res)
---------------------------------------------------------------------------------------------------------------------------
n=1004
strn=str(n)
res= ''
for i in range(len(strn)):
    if strn[i]=='0':
        res=res + '5'
    else:
        res=res+ strn[i]
print(res)        
