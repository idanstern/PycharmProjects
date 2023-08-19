prefix = "my name is"
names = ["ofek", "idan", "eden", "aviran", "avidan", "daniel"]
for name in names:
    name = name + "z"
    print(f"{prefix} {name}")

for i in range(len(names)):
    names[i] = names[i] +"z"
    print(f"{prefix} {names[i]}")

    print(names)
    result = []
    for name in names:
        if name.find("dan") > -1:
            result.append(name)

my_other_result = [name for name in names if name.find("dan") > -1]
print(result)
print(my_other_result)

age = int(input("enter your age"))
while age < 50:
    print("you are still ok")
    age = int(input("enter your age"))
