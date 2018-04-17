#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Crystal.Game')
def gem():
    require_gem('Crystal.BlankSquare')
    require_gem('Crystal.Board')
    require_gem('Crystal.ChessKing')
    require_gem('Crystal.Core')
    require_gem('Crystal.FrozenChessKing')
    require_gem('Crystal.Player')
    require_gem('Crystal.Square')
    require_gem('Crystal.VoidSquare')


    def command_test():
        line('ZAK: %s', conjure_frozen_ally_chess_king(20, 20))


    def command_dump():
        pass
        #line('store_v0:  %s', store_v0)


    @share
    def command_game():
        command_test()
        command_dump()

        board = GameBoard(1, alice, create_enemy_chess_king(), create_ally_chess_king())

        board.dump_abbreviation()

        board.actions()
        line('---')
        board.dump_abbreviation()
