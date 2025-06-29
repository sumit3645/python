age=int(input("enter your age "))
day=input("enter the week day(mon,tue,wed) ")

price= 12 if age >=18 else 8

if day=="wed":
    price=price-2
print(price)
