import datetime 

time = datetime.datetime.now()
time.hour
name = input("Enter your Name: ")

if time.hour < 12:
    print("\nGood Morning 🌄️ 🌄️ ", name)
elif 12 <= time.hour < 18:
    print("\nGood Afternoon 🌅️ 🌅️ ", name)
else:
    print("\nGood Evening 🌇️ 🌇️ ", name)
    
print("")


