# Peasant Revolt Chess
opposite_color = {'Black': 'White',
                  'White': 'Black'}

def change_position( old_pos, col_delta, row_delta ):
    new_col = chr( ord(old_pos[0]) + col_delta )
    new_row = chr( ord(old_pos[1]) + row_delta )
    return new_col + new_row

def create_game( ):
    game = {'turn': 'White'}
    for col in 'abcdefgh':
        for row in '12345678':
            game[col + row] = '-'
    for col in 'abcdefgh':
        game[col + '2'] = 'White:Pawn'
    game['e1'] = 'White:King'
    game['b8'] = 'Black:Knight'
    game['c8'] = 'Black:Knight'
    game['e8'] = 'Black:King'
    game['g8'] = 'Black:Knight'
    game['e7'] = 'Black:Pawn'
    return game

def get_square( game, position ):
    return game[position]

def get_game_status( game ):
    if 'White:King' not in game.values( ):
        return -1
    elif 'Black:King' not in game.values( ):
        return 1
    else:
        return 0

def pawn_moves( game, position ):
    moves = []

    if 'White' in game[position]:
        row_offset =1
    else:
        row_offset = -1

    for col_offset in [-1, 1]:
        new_pos = change_position( position, col_offset, row_offset )
        if new_pos in game and opposite_color[game['turn']] in game[new_pos]:
            moves.append( new_pos )

    new_pos = change_position( position, 0, row_offset )
    if new_pos in game and game[new_pos] == '-':
        moves.append( new_pos )

    return moves

def king_moves( game, position ):
    moves = []

    for col_offset in range( -1, 2 ):
        for row_offset in range( -1, 2 ):
            new_pos = change_position( position, col_offset, row_offset )
            if new_pos in game and game['turn'] not in game[new_pos]:
                moves.append( new_pos )

    return moves

def knight_moves( game, position ):
    moves = []

    for offset_1 in [2, -2]:
        for offset_2 in [1, -1]:
            new_pos = change_position( position, offset_1, offset_2 )
            if new_pos in game and game['turn'] not in game[new_pos]:
                moves.append( new_pos )

            new_pos = change_position( position, offset_2, offset_1 )
            if new_pos in game and game['turn'] not in game[new_pos]:
                moves.append( new_pos )

    return moves

def get_possible_moves( game, position ):
    moves = []
    if get_game_status( game ) == 0 and game['turn'] in game[position]:
        if 'Pawn' in game[position]:
            moves = pawn_moves( game, position )
        elif 'King' in game[position]:
            moves = king_moves( game, position )
        elif 'Knight' in game[position]:
            moves = knight_moves( game, position )
    return moves

def make_move( game, start, end ):
    if end in get_possible_moves( game, start ):
        game[end] = game[start]
        game[start] = '-'
        game['turn'] = opposite_color[game['turn']]

if __name__ == '__main__':
    game = create_game( )
