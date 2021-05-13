def count_week():
    ls = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    count = 0
    while count < 7:
        yield ls[count]
        count += 1

week = count_week()
for num in week:
    print(num)

print(range())