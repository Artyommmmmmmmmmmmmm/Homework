list1 =[0, 1, 2]
pos = {1 : '-', 2 : '-', 3 : '-',
       4 : '-', 5 : '-', 6 : '-',
       7 : '-', 8 : '-', 9 : '-'}

movelist = []




while True:
    print(' ', *list1)
    print(list1[0], pos[1], pos[2], pos[3])
    print(list1[1], pos[4], pos[5], pos[6])
    print(list1[2], pos[7], pos[8], pos[9])
    p1move = int(input('Игрок 1, куда вы хотите поставить крестик (1-9):'))

    if p1move in movelist:
        p1move = int(input('Выберите пустую позицию иначе ход перейдёт к следующему игроку!:'))
        if p1move not in movelist:
            pos[p1move] = 'X'
    else:
        movelist.append(p1move)
        pos[p1move] = 'X'

    print(' ', *list1)
    print(list1[0], pos[1], pos[2], pos[3])
    print(list1[1], pos[4], pos[5], pos[6])
    print(list1[2], pos[7], pos[8], pos[9])   

    if pos[1] == 'X' and pos[2] == 'X' and pos[3] == 'X' or\
       pos[4] == 'X' and pos[5] == 'X' and pos[6] == 'X' or\
       pos[7] == 'X' and pos[8] == 'X' and pos[9] == 'X' or\
       pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X' or\
       pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X' or\
       pos[3] == 'X' and pos[6] == 'X' and pos[9] == 'X' or\
       pos[1] == 'X' and pos[5] == 'X' and pos[9] == 'X' or\
       pos[7] == 'X' and pos[5] == 'X' and pos[3] == 'X':
     
        print('Игрок 1 одержал победу!')
        break

    if '-' not in pos.values():
        print('Ничья!')
        break

    p2move = int(input('игрок 2, куда вы хотите поставить нолик (1-9):'))

    if p2move in movelist:
        p2move = int(input('Выберите пустую позицию иначе ход перейдёт к следующему игроку!:'))
        if p2move not in movelist:
            pos[p2move] = 'O'
    else:
        movelist.append(p2move)
        pos[p2move] = 'O'
    
    print(' ', *list1)
    print(list1[0], pos[1], pos[2], pos[3])
    print(list1[1], pos[4], pos[5], pos[6])
    print(list1[2], pos[7], pos[8], pos[9])   

    if pos[1] == 'O' and pos[2] == 'O' and pos[3] == 'O' or\
       pos[4] == 'O' and pos[5] == 'O' and pos[6] == 'O' or\
       pos[7] == 'O' and pos[8] == 'O' and pos[9] == 'O' or\
       pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O' or\
       pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O' or\
       pos[3] == 'O' and pos[6] == 'O' and pos[9] == 'O' or\
       pos[1] == 'O' and pos[5] == 'O' and pos[9] == 'O' or\
       pos[7] == 'O' and pos[5] == 'O' and pos[3] == 'O':
        print(' ', *list1)
        print(list1[0], pos[1], pos[2], pos[3])
        print(list1[1], pos[4], pos[5], pos[6])
        print(list1[2], pos[7], pos[8], pos[9])
        print('Игрок 2 одержал победу!')
        break

    







