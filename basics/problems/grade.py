score=int(input("enter the score: "))
if score > 100:
    print("it's should not be greter than 100")
    exit()
if score > 90:
    grade="A"
elif score > 80:
    grade="B"
else:
    grade="C"            
print(f"your grade is:" ,grade)
