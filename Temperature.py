#First program using user input

def weather(temp):
    if temp >= 85.0:
        temp2 = "The weather is hot"
    elif 84.0 >= temp >= 70.0:
        temp2 = "The weather is warm"
    else:
        temp2 = "The weather is cold."
    return temp2


user_input = float(input("What is the temperature?"))

print(weather(user_input))