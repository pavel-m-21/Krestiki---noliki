#крестики - нолики
a = [[' ', '0', '1', '2'],
     ['0', '-', '-', '-'],
     ['1', '-', '-', '-'],
     ['2', '-', '-', '-']
     ]
print("Игра крестики - нолики 3x3")
def table(x):
    for i in x:
        for b in i:
            print(b, end=" ")
        print()
table(a)

def igrok_x():
    while True:
        print("Игрок X выбери строку и столбец")
        stroka = int(input("Выбери строку 0, 1 или 2: "))
        stolbets = int(input("Выбери столбец 0, 1 или 2: "))
        if (stroka >= 3 or stolbets >= 3):
            print("Такого поля нет")
        elif (a[stroka + 1][stolbets + 1] == "O") or (a[stroka + 1][stolbets + 1] == "X"):
            print("Поле занято")
        else:
            a[stroka + 1][stolbets + 1] = "X"
            break

def igrok_O():
    while True:
        print("Игрок O выбери строку и столбец")
        stroka = int(input("Выбери строку 0, 1 или 2: "))
        stolbets = int(input("Выбери столбец 0, 1 или 2: "))
        if (stroka >= 3 or stolbets >= 3):
            print("Такого поля нет")
        elif (a[stroka + 1][stolbets + 1] == "O") or (a[stroka + 1][stolbets + 1] == "X"):
            print("Поле занято")
        else:
            a[stroka + 1][stolbets + 1] = "O"
            break

while True:
    igrok_x()
    table(a)
    if (a[1][1] == "X" and a[1][2] == "X" and a[1][3] == "X") or (
            a[2][1] == "X" and a[2][2] == "X" and a[2][3] == "X") or (
            a[3][1] == "X" and a[3][2] == "X" and a[3][3] == "X") or (
            a[1][1] == "X" and a[2][1] == "X" and a[3][1] == "X") or (
            a[1][2] == "X" and a[2][2] == "X" and a[3][2] == "X") or (
            a[1][3] == "X" and a[2][3] == "X" and a[3][3] == "X") or (
            a[1][3] == "X" and a[2][3] == "X" and a[3][3] == "X") or (
            a[1][1] == "X" and a[2][2] == "X" and a[3][3] == "X") or (
            a[1][3] == "X" and a[2][2] == "X" and a[3][1] == "X"):
        print("Победил игрок X")
        break
    elif all([h != '-' for i in a for h in i]):
        print("Ничья")
        break
    igrok_O()
    table(a)
    if (a[1][1] == "O" and a[1][2] == "O" and a[1][3] == "O") or (
            a[2][1] == "O" and a[2][2] == "O" and a[2][3] == "O") or (
            a[3][1] == "O" and a[3][2] == "O" and a[3][3] == "O") or (
            a[1][1] == "O" and a[2][1] == "O" and a[3][1] == "O") or (
            a[1][2] == "O" and a[2][2] == "O" and a[3][2] == "O") or (
            a[1][3] == "O" and a[2][3] == "O" and a[3][3] == "O") or (
            a[1][3] == "O" and a[2][3] == "O" and a[3][3] == "O") or (
            a[1][1] == "O" and a[2][2] == "O" and a[3][3] == "O") or (
            a[1][3] == "O" and a[2][2] == "O" and a[3][1] == "O"):
        print("Победил игрок O")
        break
    elif all([h != '-' for i in a for h in i]):
        print("Ничья")
        break