s='sumit'
res={}
def isIsogram(s):
    for char in s:
        if char in res:
            return 0
        else:
            res[char]=1
    return 1      
print(isIsogram('machine')) 
---------------------------------------------------------------------------
for i in range(len(s)):
    val=s[i]
    for j in range(i+1,len(s)):
        val2=s[j]
        if val==val2:
            print(0)
        else:
            continue
        
