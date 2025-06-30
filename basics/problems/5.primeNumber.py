number=int(input("enter the number: "))
is_prime= True
if (number==0 or number==1):
    is_prime=False

if number > 1:
    for i in range(2,number):
        if number % i ==0:
            is_prime=False
            break
print(is_prime)        



number=int(input("enter the number: "))
if number==0 and number==1:
    print("not prime")
if number >1:
    for i in range(2,number):
        if number % i ==0:
            print("not prime")
            break
    else:
        print("prime")    



number=int(input("enter the number: "))
for num in range(number+1):
    if num >1:
        for i in range(2,num):
            if num % i==0:
                break
        else:
            print(num)    

    
