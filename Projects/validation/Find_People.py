in_name = input("Enter Name: ")
myfile_2 =open('names.txt')
lines = myfile_2.readlines()
found = False
for line in lines:
    t_name = line.split(",")
    name = t_name.pop(0)
    if in_name == name:
        found = True
if found :
    print(in_name,'is not on Hoofle..')

else:
    print('Could not find user..')
