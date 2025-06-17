# # Initial function

# def greet():
#     print("Hello!")
#     print("How are you doing?")
#     print("What's going on?")

# greet()    

# # Functions that allows for inputs

# def greet_with_name(name):
#     print(f"Hello! {name}")
#     print(f"How are you doing? {name}")
#     print(f"What's going on? {name}")

# greet_with_name("Vinicius")    

# def greet_with(name, location):
#     print(f"Hi, name is {name} and I'm currently living in {location}.")

# greet_with("Vinicius", "Cork, Ireland")

def greet_with(name, location, age):
    print(f"Hi, my name is {name}.")
    print(f"I'm currently living in {location}.")
    print(f"My age is {age} years old.")

greet_with(location="Ireland", age=27, name="Vinicius")    