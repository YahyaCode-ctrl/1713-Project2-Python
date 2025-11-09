#En aquest arxiu, apprendrem a practicar noves coses en Python.
age=int(input("How old are you: "))
while age < 0:
    print(f"an {age} cannot be negative")
    age=int(input("How old are you: "))
print(f"You are {age} old !!")