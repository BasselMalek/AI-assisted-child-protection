import json

blacklist = []

while True:
    print("\nProject CABCP V0.1\nGeneral Moderation Blacklist Generator\n1. Enter new entry\n2. Print current list\n3. Exit")
    response = input()
    if (response == "1"):
        word = input("New entry: ")
        blacklist.append(word)
        continue
    elif (response == "2"):
        print(blacklist)
        continue
    elif (response == "3"):
        break
    else:
        print("Invalid choice, exiting...")
        break

with open("D:\\Code\\Fuck_Me\\Databases\\blacklist.txt", "w") as j:
    json.dump(blacklist, j)