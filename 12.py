my_file = open("names.txt")
names = my_file.readlines()
print(names)

my_file.close()

print("aviel")

my_file2 = open("names.txt", 'a+')
for i in range(3):
    my_file2.write(input("enter name: ") + "\n")