weather_case = input("What's the weather like today? (sunny/rainy/cold):").lower().strip()

if weather_case == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_case == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_case == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else :
    print("Sorry, I don't have recommendations for this weather.")

