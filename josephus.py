from collections import deque
from random import randint

names = ["Charlie", "Moe", "Curly", "Shirley", "Whirly", "Nurt", "Stranger", "Seutonius", "Caesar", "Billfinger", "Job", "Isaac", "Napoleon", "Camus", "Unnammed Man", "Gurt", "Frank 16", "Albert", "Bob", "Ann", "Lisa", "Billy", "23", "Aaron", "Jared", "Susan", "Jeb", "Donald", "Bernie", "30", "Josephus", "Manfield", "Yoda", "Luke", "Leia", "Adam", "Eve", "Toby", "Dalton", "Percy"]
qq = deque()

def josephus(names, m):
    for name in names:
        qq.append(name)
    count = 0
    while len(qq) > 1:
        count = count + 1
        name = qq.popleft()
        if count != m:
            qq.append(name)
            print('\033[92m', count, name, "was skipped.", '\033[0m')
        else:
            print('\033[91m', count, name, "was murdered.", '\033[0m')
            print(" ")
            count = 0
    print(" ")
    print(qq.popleft() + " survived.")

josephus(names, randint(1,13))
