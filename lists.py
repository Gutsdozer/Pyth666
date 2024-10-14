my_list = [1, 2, 4, 7, 12, 'text', False, 2.1]
print(my_list[0])
my_list[5] = 42
print(my_list)
my_list.append('text')
print(my_list)


for element in my_list:
    print(element)

    numbers = [1,2,3,4,5,6]
    for x in numbers:
        if x>3:
            print(x*2)
        elif x>2:
            print(x*3)
        else:
            print(x)


my_tuple = (1, 2, 5, 7, 'text')
print(my_tuple[3])
for element in my_tuple:
    print(element)

my_dict = {'name': 'Bob', 'phone': 123}
print(my_dict['name'])
my_dict['phone'] = 345
print(my_dict)

for element in my_dict:
    print(element)

for key in my_dict:
    print(my_dict[key])
    print(key, my_dict[key])