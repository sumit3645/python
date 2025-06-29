password=input("enter your password: ")
pass_lenght= len(password)
if pass_lenght < 5:
    strenght="weak"
elif pass_lenght <= 10:
    strenght="mediam"
else:
    strenght="strong"    
print("password strenght is: ", strenght)    
