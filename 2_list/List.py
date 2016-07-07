name = "Hello"
lst = list(name)
print(lst)

lst[0] = "h"
print(lst)

del lst[2]
print(lst)

lst[2:2] = list("l")
print(lst)

print(len(lst))

lst[2:] = list("y, you there!")
print(lst)

lst[3:] = []
print(lst)

lst.append("!")
print(lst)

print(lst.count("e"))

lst.extend(list(" You there?"))
print(lst)
