weather=input("what is condition of weather(sunny,rainy,snow): ")
lower_weather=weather.lower()
if lower_weather == "sunny":
    activity= "go for walk"
elif lower_weather == "rainy":
    activity = "read a book"
else:
    activity= "watch netflix"
print(activity)            
