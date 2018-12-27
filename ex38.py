ten_things = "Apples Oranges Crows Telphone Light Sugar"

print("Wait there's not 10 thing in that list, lets fix that.")

existing_list = ten_things.split(' ')
new_list = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(existing_list) != 10:
    next_item = new_list.pop()
    print("There we go: ", next_item)
    existing_list.append(next_item)
    print("There's %d items now" % len(existing_list))

print("There we go: ", existing_list)

print("Let's do some things with the existing list.")

print(existing_list[1])
print(existing_list[-1])
print(existing_list.pop())
print(' '.join(existing_list))
print('#'.join(existing_list[3:5]))