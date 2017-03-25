from collections import deque
from random import randint

names = ["Charlie", "Moe", "Curly", "Shirley", "Whirly", "Nurt", "Stranger", "Seutonius", "Caesar", "Billfinger", "Job", "Isaac", "Napoleon", "Camus", "Unnammed Man", "Gurt", "Frank 16", "Albert", "Bob", "Ann", "Lisa", "Billy", "23", "Aaron", "Jared", "Susan", "Jeb", "Donald", "Bernie", "30", "Josephus", "Manfield", "Yoda", "Luke", "Leia", "Adam", "Eve", "Toby", "Dalton", "Percy"]
qq = deque()

def josephus(names, m):
    for name in names:
        qq.append(name)
    count = 0
    roun = 0
    while len(qq) > 1:
        count = count + 1
        name = qq.popleft()
        if count != m:
            qq.append(name)
            print(count,'\033[92m', '\033[93m', name, '\033[0m', "was skipped.", '\033[0m')
        else:
            roun = roun + 1
            print(count, '\033[91m', name, "was murdered", '\033[0m', "in round ", roun, ".")
            print(" ")
            count = 0

    print(" ")
    print('\033[94m', qq.popleft(), '\033[0m', "survived", roun + 1, "rounds,")
    print(" ")
    print(" ")

josephus(names, randint(1,40))
