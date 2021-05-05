names = ["carlos", "linda", "numibia", "lucas", "suelen", "christiana"]

new = [f"The long name {name}" for name in names if len(name) > 5]

print(new)