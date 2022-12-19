field = [[' ' for i in range(3)] for j in range(3)]

def out():
    print('   | 0 | 1 | 2 |')
    for i in range(3):
        print(f' {i} |', ' | '.join(field[i]), '|')



def input_():
    while True:
        list_input = input('Input your move: ').split()

        if len(list_input) != 2:
            print('Input two numbers')
            continue

        x = list_input[0]
        y = list_input[1]

        if not (x.isdigit() and y.isdigit()):
            print('Input two numbers')
            continue

        x = int(x)
        y = int(y)

        if not (0<=x<=2 and 0<=y<=2):
            print('Out of range')
            continue

        if field[x][y] != ' ':
            print('cell is occupied')
            continue

        return x,y
        break

def win():
    win_comb = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)), ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0)))
    for x,y,z in win_comb:
        if field[x[0]][x[1]] == field[y[0]][y[1]] == field[z[0]][z[1]] == 'X':
            print('X WIN!')
            return True
        if field[x[0]][x[1]] == field[y[0]][y[1]] == field[z[0]][z[1]] == '0':
            print('0 WIN!')
            return True
    return False

for counter in range(9):
    out()
    x,y = input_()

    if counter%2 == 0:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    if counter == 8:
        print('DRAW!')
    if win():
        break