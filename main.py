
def print_field(field_):
    if field_ == player_field:
        print('поле игрока:')
    if field_ == computer_field:
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


player_field = [['0' for x in range(6)] for y in range(6)]
computer_field = [['0' for x1 in range(6)] for y1 in range(6)]

# player_field[0][0] = '■'
# print_field(player_field)
# print_field(computer_field)
