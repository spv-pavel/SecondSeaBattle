
def field_print(field_):
    if field_ == field_player:
        print('поле игрока:')
    if field_ == field_computer:
        print('поле компьютера:')
    print('  |', end=' ')
    for i_ in range(1, len(field_[0]) + 1):
        print(i_, '|', end=' ')
    print('\n', end='')
    for ny_, y_ in enumerate(range(len(field_))):
        print(ny_ + 1, '|', end=' ')
        for x_ in range(len(field_[y_])):
            print(field_[y_][x_], '|', end=' ')
        print('\n', end='')
    return ''


field_player = [['0' for x in range(6)] for y in range(6)]
field_computer = [['0' for x1 in range(6)] for y1 in range(6)]

field_player[0][0] = '■'
# field_print(field_player)
# field_print(field_computer)
