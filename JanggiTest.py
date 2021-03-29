import unittest
from JanggiGame import Board, Soldier, Guard, Chariot, Cannon, Horse, Elephant, JanggiGame

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.b = Board()

    def test_convert_coords(self):
        self.assertEqual(self.b.convert_coords('a1'), (0, 0))
        self.assertIsNone(self.b.convert_coords('j1'))
        self.assertIsNone(self.b.convert_coords('c11'))
        self.assertEqual(self.b.convert_coords('i10'), (9, 8))

class SoldierTest(unittest.TestCase):
    def setUp(self):
        self.sr = Soldier('red', 'redsold', 'soldier', (3, 0))
        self.sr2 = Soldier('red', 'soldred', 'soldier', (3, 2))
        self.sr3 = Soldier('red', 'red', 'soldier',(7, 3))
        self.sr3._in_palace = True
        self.sb = Soldier('blue', 'bluesold', 'soldier',(6, 0))
        self.sb2 = Soldier('blue', 'blue', 'soldier',(6, 2))
        self.sb3 = Soldier('blue', 'blue', 'soldier',(2, 3))
        self.sb3._in_palace = True

    def test_soldier_moves_red(self):
        # red vertical moves
        self.assertTrue(self.sr.valid_move((4,0)))
        self.assertFalse(self.sr.valid_move((2,0)))
        self.assertFalse(self.sr.valid_move((5, 0)))
        self.assertFalse(self.sr.valid_move((4, 1)))

        # red horizontal moves
        self.assertTrue(self.sr2.valid_move((3, 1)))
        self.assertTrue(self.sr2.valid_move((3, 3)))
        self.assertFalse(self.sr2.valid_move((3, 0)))

        # red palace moves
        self.assertTrue(self.sr3.valid_move((8, 4)))
        self.sr3.set_location((7, 5))
        self.assertTrue(self.sr3.valid_move((8, 4)))
        self.sr3.set_location((8, 4))
        self.assertTrue(self.sr3.valid_move((9, 3)))
        self.assertTrue(self.sr3.valid_move((9, 5)))
        
    def test_soldier_moves_blue(self):
        # blue vertical moves
        self.assertTrue(self.sb.valid_move((5, 0)))
        self.assertFalse(self.sb.valid_move((7, 0)))
        self.assertFalse(self.sb.valid_move((4, 0)))
        self.assertFalse(self.sb.valid_move((5, 1)))

        # blue horizaontal moves
        self.assertTrue(self.sb2.valid_move((6, 1)))
        self.assertTrue(self.sb2.valid_move((6, 1)))
        self.assertFalse(self.sb2.valid_move((6, 0)))

        # blue palace moves
        self.assertTrue(self.sb3.valid_move((1, 4)))
        self.sb3.set_location((2, 5))
        self.assertTrue(self.sb3.valid_move((1, 4)))
        self.sb3.set_location((1, 4))
        self.assertTrue(self.sb3.valid_move((0, 5)))
        self.assertTrue(self.sb3.valid_move((0, 3)))

class MasterValidMove(unittest.TestCase):
    def setUp(self):
        self.bg = Guard('blue', 'blue', 'soldier',(9, 3))
        self.bg2 = Guard('blue', 'blue', 'soldier',(7, 5))
        self.rg = Guard('red', 'red', 'soldier',(0, 3))
        self.rg2 = Guard('red', 'red', 'soldier',(2, 5))

    def test_blue(self):
        self.assertTrue(self.bg.valid_move((8, 4)))   
        self.assertFalse(self.bg.valid_move((9, 2)))
        self.assertTrue(self.bg.valid_move((8, 3))) 
        self.assertTrue(self.bg2.valid_move((8, 4)))
        self.assertTrue(self.bg2.valid_move((8, 5)))

    def test_red(self):
        self.assertTrue(self.rg.valid_move((1, 4)))
        self.assertTrue(self.rg.valid_move((0, 4)))
        self.assertTrue(self.rg2.valid_move((1, 4)))
        self.assertTrue(self.rg2.valid_move((2, 4)))
        self.assertFalse(self.rg.valid_move((0, 2)))

class ChariotMove(unittest.TestCase):
    def setUp(self):
        self.rc = Chariot('red', 'red','soldier', (0, 0))
        self.rc2 = Chariot('red', 'red', 'soldier',(0, 3))
        self.bc = Chariot('blue', 'blue', 'soldier',(9, 0))
        self.bc2 = Chariot('blue', 'blue', 'soldier',(7, 3))
    
    def test_red(self):
        self.assertFalse(self.rc.valid_move((1, 1)))
        self.assertTrue(self.rc.valid_move((0, 8)))
        self.assertTrue(self.rc.valid_move((9, 0)))
        self.assertTrue(self.rc2.valid_move((2, 5)))
        self.assertTrue(self.rc2.valid_move((9, 3)))
        self.assertFalse(self.rc2.valid_move((3, 0)))
    
    def test_blue(self):
        self.assertFalse(self.bc.valid_move((8, 2)))
        self.assertTrue(self.bc.valid_move((9, 8)))
        self.assertTrue(self.bc.valid_move((0, 0)))
        self.assertTrue(self.bc2.valid_move((9, 5)))
        self.assertTrue(self.bc2.valid_move((0, 3)))

class CannonMove(unittest.TestCase):
    def setUp(self):
        self.rc = Cannon('red', 'red','soldier', (2, 7))
        self.rc2 = Cannon('red', 'red', 'soldier',(0, 3))
    
    def test_red(self):
        self.assertFalse(self.rc.valid_move((2, 8)))
        self.assertTrue(self.rc.valid_move((4, 7)))
        self.assertFalse(self.rc2.valid_move((1, 4)))
        self.assertTrue(self.rc2.valid_move((2, 5)))

class HorseMove(unittest.TestCase):
    def setUp(self):
        self.rh = Horse('red', 'red', 'soldier',(0, 2))
        self.bh = Horse('blue', 'blue','soldier', (9, 7))

    def test_move(self):
        self.assertTrue(self.rh.valid_move((2, 1)))
        self.assertFalse(self.rh.valid_move((0, 3)))
        self.assertFalse(self.rh.valid_move((0, 1)))
        self.assertFalse(self.rh.valid_move((1, 3)))
        self.assertTrue(self.bh.valid_move((8, 5)))

class ElephantMove(unittest.TestCase):
    def setUp(self):
        self.re = Elephant('red', 'red', 'soldier',(0, 1))
        self.be = Elephant('blue', 'blue','soldier', (9, 6))

    def test_move(self):
        self.assertTrue(self.re.valid_move((3, 3)))
        self.assertFalse(self.re.valid_move((2, 0)))
        self.assertTrue(self.be.valid_move((7, 3)))
        self.assertFalse(self.be.valid_move((7, 2)))

class BlockedTest(unittest.TestCase):
    def setUp(self):
        self.g = JanggiGame()
    
    def test_guard_gen_block(self):
        guard = self.g._board.get_piece((9, 3))
        gen = self.g._board.get_piece((1, 4))
        self.assertTrue(guard.is_blocked((8, 4), self.g._board))
        self.assertFalse(guard.is_blocked((8, 3), self.g._board))
        self.assertTrue(gen.is_blocked((0, 5), self.g._board))
        self.assertFalse(gen.is_blocked((2, 3), self.g._board))
    
    def test_chariot_block(self):
        char = self.g._board.get_piece((0, 0))
        char2 = self.g._board.get_piece((9, 0))
        char2._location = (7, 3)
        char3 = self.g._board.get_piece((9, 8))
        self.assertFalse(char.is_blocked((2, 0), self.g._board))
        self.assertTrue(char.is_blocked((3, 0), self.g._board))
        self.assertFalse(char2.is_blocked((7, 6), self.g._board))
        self.assertTrue(char2.is_blocked((7, 7), self.g._board))
        char2._location = (9, 3)
        self.assertTrue(char2.is_blocked((7, 5), self.g._board))
        self.g._board.remove_piece((8, 4))
        self.assertFalse(char2.is_blocked((8, 4), self.g._board))

    def test_cannon_block(self):
        redcan = self.g._board.get_piece((2, 1))
        self.assertTrue(redcan.is_blocked((5, 1), self.g._board))
        self.assertTrue(redcan.is_blocked((9, 1), self.g._board))
        redcan.set_location((2, 2))
        self.assertFalse(redcan.is_blocked((4, 2), self.g._board))
        redcan.set_location((7, 3))
        self.assertFalse(redcan.is_blocked((9, 5), self.g._board))

    def test_horse_block(self):
        bh = self.g._board.get_piece((9, 2))
        rh = self.g._board.get_piece((0, 7))
        self.assertTrue(bh.is_blocked((8, 0), self.g._board))
        self.assertFalse(bh.is_blocked((7, 3), self.g._board))
        self.assertTrue(rh.is_blocked((1, 5), self.g._board))

    def test_elephant_block(self):
        be = self.g._board.get_piece((9, 1))
        self.assertFalse(be.is_blocked((6, 3), self.g._board))
        self.assertTrue(be.is_blocked((7, 4), self.g._board))
        re = self.g._board.get_piece((0, 1))
        re.set_location((2, 2))
        self.assertTrue(re.is_blocked((4, 5), self.g._board))

class GameTest(unittest.TestCase):
    def setUp(self):
        self.g = JanggiGame()
    
    def test_pass_turn(self):
        self.g.make_move('e1', 'e1')
        self.assertEqual(self.g.get_player_turn(), 'red')
    
    def test_red_check(self):
        self.g.make_move('c10', 'd8')
        self.g.make_move('e4', 'f4')
        self.g.make_move('b8', 'e8')
        self.assertTrue(self.g.is_in_check('red'))
    
    def test_blue_check(self):
        self.g.make_move('e7', 'f7')
        self.g.make_move('e4', 'd4')
        self.g.make_move('a7', 'a7')
        self.g.make_move('e2', 'e1')
        self.g.make_move('a7', 'a7')
        self.g.make_move('a1', 'a2')
        self.g.make_move('a7', 'a7')
        self.g.make_move('a2', 'e2')
        self.assertTrue(self.g.is_in_check('blue'))
    
    def test_checkmate(self):
        self.g.make_move('a7', 'b7')
        self.g.make_move('i4', 'h4')
        self.g.make_move('h10', 'g8')
        self.g.make_move('c1', 'd3')
        self.g.make_move('h8', 'e8')
        self.g.make_move('i1', 'i2')
        self.g.make_move('e7', 'f7')
        self.g.make_move('b3', 'e3')
        self.g.make_move('g10', 'e7')
        self.g.make_move('e4', 'd4')
        self.g.make_move('c10', 'd8')
        self.g.make_move('g1', 'e4')
        self.g.make_move('f10', 'f9')
        self.g.make_move('h1', 'g3')
        self.g.make_move('a10', 'a6')
        self.g.make_move('d4', 'd5')
        self.g.make_move('e9', 'f10')
        self.g.make_move('h3', 'f3')
        self.g.make_move('e8', 'h8')
        self.g.make_move('i2', 'h2')
        self.g.make_move('h8', 'f8')
        self.g.make_move('f1', 'f2')
        self.g.make_move('b8', 'e8')
        self.g.make_move('f3', 'f1')
        self.g.make_move('i7', 'h7')
        self.g.make_move('f1', 'c1')
        self.g.make_move('d10', 'e9')
        self.g.make_move('a4', 'b4')
        self.g.make_move('a6', 'a1')
        self.g.make_move('c1', 'a1')
        self.g.make_move('f8', 'd10')
        self.g.make_move('d5', 'c5')
        self.g.make_move('i10', 'i6')
        self.g.make_move('b1', 'd4')
        self.g.make_move('c7', 'c6')
        self.g.make_move('c5', 'b5')
        self.g.make_move('b10', 'd7')
        self.g.make_move('d4', 'f7')
        self.g.make_move('g7', 'f7')
        self.g.make_move('a1', 'f1')
        self.g.make_move('g8', 'f6')
        self.g.make_move('f1', 'f5')
        self.g.make_move('f6', 'd5')
        self.g.make_move('e3', 'e5')
        self.g.make_move('f7', 'f6')
        self.g.make_move('f5', 'f7')
        self.g.make_move('f10', 'e10')
        self.g.make_move('e2', 'f1')
        self.g.make_move('i6', 'i3')
        self.g.make_move('h2', 'g2')
        self.g.make_move('i3', 'i1')
        self.g.make_move('f1', 'e2')
        self.g.make_move('f6', 'f5')
        self.g.make_move('c4', 'd4')
        self.g.make_move('f5', 'e5')
        self.g.make_move('f7', 'd7')
        self.g.make_move('e7', 'g4')
        self.g.make_move('d4', 'd5')
        self.g.make_move('e5', 'e4')
        self.g.make_move('d3', 'e5')
        self.g.make_move('e4', 'e3')
        self.g.make_move('e2', 'd2')
        self.g.make_move('e3', 'e2')
        self.g.make_move('d2', 'd3')
        self.g.make_move('e8', 'e4')
        self.g.make_move('f2', 'e2')
        self.g.make_move('i1', 'd1')
        self.g.make_move('e2', 'd2')
        self.g.make_move('d1', 'f3')
        self.assertTrue(self.g.get_game_state(), 'BLUE_WON')


if __name__ == '__main__':
    unittest.main()
