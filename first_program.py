#This is not a particularly useful program, but I id get to combine things I've learned such as lists, user input, etc.

def maker(phrase):
    interrogative = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    user_input = input("Say something:")
    if user_input == "/end":
        break
    else:
        results.append(maker(user_input))

print(" ".join(results))
