try:
    inp = int(input("what day is today?"));
except:
    inp = "not a number"

if(type(inp) == str):
    print(inp)
else:
    if(inp == 31):
        out = 1
    else:   
        out = inp + 1

    print("tomorrow will be", out)

marcia = None
print(marcia)

# dic = {}

# dic["car"] = "Porsche"

# print(dic)

print(15/12)


open