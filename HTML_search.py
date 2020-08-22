import json
def website_linter():
    discovered_words = []
    with open("D:\\Code\\AI-assisted child protection\\Databases\\blacklist.txt", "r") as file_1:
        blacklist = json.load(file_1)
        file_1.close()


    with open('cache.html','r') as file_2: 
        for line in file_2: 
           for word in line.split():
               if (word in blacklist):
                   discovered_words.append(word)
        file_2.close()


    if (len(discovered_words) == 0):
        return False
    else:
        file_3 = open("D:\\Code\\AI-assisted child protection\\Databases\\discovered_words.txt", "r")
        json.dump(discovered_words, file_3)
        return True

    