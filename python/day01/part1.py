filename = "input.txt"
# filename = "example.txt" 

with open(filename, "r") as file:
    max_calories = 0
    temp = 0
    for line in file.readlines():
        if line.strip() == '':
            max_calories = max(max_calories, temp)
            temp = 0 
        else: 
            temp += int(line.strip())

print(max_calories)
