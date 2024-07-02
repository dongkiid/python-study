line = input()
happy = line.count(":-)")
sad = line.count(":-(")
# 둘 다 포함되어 있지 않은 경우
if happy == 0 and sad == 0:
    print("none")
else:
    if happy < sad:
        print("sad")
    elif happy > sad:
        print("happy")
    elif happy == sad:
        print("unsure")