from functools import wraps

# def enforce_fries(fn):
#     wraps(fn)
#     def wrapper(*args, **kwargs):
#         if args[0] != "fries":
#             return "You must love fries before everything else"
#         return fn(*args, **kwargs) 
#     return wrapper


# @enforce_fries
# def eat(first_dish, second_dish):
#     return f"Hello, I may not know you well, but let me say that I love {first_dish} and {second_dish}"

# print(eat("frie", "bacon"))

def say_two(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs) + " and hello to you too Tim!"
    return wrapper

@say_two
def say_one(name, place):
    return f"Hello {name} from {place}"

# greet = say_two(say_one)
# print(greet("Mary"))

# print(say_two(say_one)("Mary"))

print(say_one("Tammy", "York"))