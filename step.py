# try:
#     inp = int(input("what day is today?"));
# except:
#     inp = "not a number"

# if(type(inp) == str):
#     print(inp)
# else:
#     if(inp == 31):
#         out = 1
#     else:   
#         out = inp + 1

#     print("tomorrow will be", out)

# marcia = None
# print(marcia)

# dic = {}

# dic["car"] = "Porsche"

# print(dic)

# def divide_by_two(num):
#     return num / 2;

# print(divide_by_two(4))


# open

def gcd(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)

print(gcd(3918848, 1653264))
