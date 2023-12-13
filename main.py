#Компьютер ходит ноликом
#Символ " обозначает пробел в формате входных данных
#Это сделано для удобства чтения данных из файла
def spisok(board):
    # создание списка, который содержит все диагонали, строки и столбцы
    lines = board
    # списки строк
    lines += [list(row) for row in board]
    # списки столбцов
    lines += [[board[i][j] for i in range(3)] for j in range(3)]
    # списки главной и побочной диагонали
    lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    # проверка на то, что строка полностью состоит из x и y
    for i in lines:
        if 'X' in i and i.count('X') == len(i):
            return 1
        elif 'O' in i and i.count('O') == len(i):
            return -1
    return 0

def findhod(board):
    # Нахождение наилучшего хода
    bznach = float('-inf')
    # Для отладки изначально присваиваю это значение
    anshod = (-90, -90)

    # Вычисление лучшего хода
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == '"':
                new_board = board
                new_board[i][j] = 'X'
                move_val = spisok(new_board)
                if move_val > bznach:
                    anshod = (i, j)
                    bznach = move_val
    return anshod

# Нужно обязательно сделать проверку на одну оставшуюся клетку. Напишем для этого функцию oneif
def oneif(bd):
    coun = 0;
    x, y = 0, 0
    for i in range(0, 3):
        for j in range(0, 3):
            if bd[i][j]=='"':
                coun += 1
                x = i
                y = j
    if coun == 1:
        print(f"Последний ход: {(x, y)}")
        exit(0)


# Открываем поле из текстового файла и заносим в двумерный массив
with open('pole.txt', 'r') as file:
    lines = file.readlines()
# Удаляем символ новой строки и разбиваем строки на символы:
bd= [list(line.strip()) for line in lines]
# Поле будет считано вот в таком формате:
# [ ['O', '"', 'O'],
#   ['X', '"', 'X'],
#   ['X', 'X', 'X'] ]
# Проверка на то, что осталась одна клетка
# Если остается одна клетка, программа прекратит свою работу
oneif(bd)

#Нахождение лучшего хода
best_move = findhod(bd)
print(f"Лучший ход: {best_move}")