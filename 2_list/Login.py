database = [
["nick", "666"],
["Judy", "888"],
["Tom", "222"],
["Lucy", "999"]
]

name = raw_input("Input yr username:\n")
pwd = raw_input("Password for:" + name + "\n")

if ([name, pwd] in database) :  print("Access granted.")
else: print("Access deny.")
