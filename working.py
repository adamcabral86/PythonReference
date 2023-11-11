with open("index.txt", "r", encoding="utf-8") as file:
    with open("index.txt", "a", encoding="utf-8") as fileAppend:

        for line in file.readlines():
            newStr = ""
            if line == "\n":
                continue
            else:
                for word in line.split(" "):
                    if word == line.split(" ")[1] or word == line.split(" ")[-1]:
                        continue
                    else:
                        newStr += word +' '
            newStr = newStr.strip()
            #for word in line.split(" "):
                #print(line.split(" "), end="")
            fileAppend.write((newStr.title()) + "\n")
            print(newStr.title())
        #print(file.read())