
import unittest
from vending_machine import Machine


class TestVendingMachine(unittest.TestCase):
    def test_no_response(self):
        m = Machine()
        self.assertEqual(m.response, [])

    def test_empty_coin_return(self):
        m = Machine()
        m.run('COIN-RETURN')
        self.assertEqual(m.response, [])

    def test_coin_insert(self):
        m = Machine()
        m.run('D')
        m.run('COIN-RETURN')
        self.assertEqual(m.response, ['D'])

    def test_coin_sum(self):
        m = Machine()
        m.run('D', 'N', 'Q')
        self.assertEqual(m.get_current_sum(), 0.4)

    def test_coin_sum_2(self):
        m = Machine()
        m.run('D', 'N', 'Q', 'Q', 'N')
        self.assertEqual(m.get_current_sum(), 0.7)

    def test_coin_insert_2(self):
        m = Machine()
        m.run('D', 'N', 'Q')
        m.run('COIN-RETURN')
        self.assertEqual(m.response, ['D', 'N', 'Q'])

    def test_coin_insert_3(self):
        m = Machine()
        m.run('Q', 'N', 'D')
        m.run('COIN-RETURN')
        self.assertEqual(m.response, ['Q', 'N', 'D'])

    def test_item_buy(self):
        m = Machine()
        m.run('Q', 'Q', 'Q', 'Q')
        m.run('BUY-B')
        self.assertEqual(m.response, ['B'])

    def test_cheat(self):
        m = Machine()
        m.run('Q')
        m.run('COIN-RETURN')
        m.run('COIN-RETURN')
        self.assertEqual(m.response, ['Q'])

    def test_item_buy_2(self):
        m = Machine()
        m.run('Q', 'Q', 'Q', 'Q', 'Q', 'Q')
        m.run('BUY-C')
        self.assertEqual(m.response, ['C'])

    def test_item_buy_3(self):
        m = Machine()
        m.run('Q', 'Q', 'D', 'N')
        m.run('BUY-A')
        self.assertEqual(m.response, ['A'])

    def test_item_buy_4(self):
        m = Machine()
        m.run('Q', 'Q', 'D', 'D', 'D', 'D', 'N', 'N')
        m.run('BUY-B')
        self.assertEqual(m.response, ['B'])

    def test_not_enough_money(self):
        m = Machine()
        m.run('Q', 'Q')
        m.run('BUY-B')
        self.assertEqual(m.response, ['Not enough money'])

    def test_item_b_available(self):
        m = Machine()
        m.run('CHECK-B')
        self.assertEqual(m.b_items, 5)

    def test_item_a_available(self):
        m = Machine()
        m.run('CHECK-A')
        self.assertEqual(m.a_items, 10)

    def test_item_c_available(self):
        m = Machine()
        m.run('CHECK-C')
        self.assertEqual(m.c_items, 15)

    def test_buy_item_b(self):
        m = Machine()
        m.run('Q', 'Q', 'D', 'D', 'D', 'D', 'N', 'N')
        m.run('BUY-B')
        self.assertEqual(m.b_items, 4)

    def test_buy_item_b2(self):
        m = Machine()
        m.run('Q', 'Q', 'D', 'D', 'D', 'D', 'N', 'N')
        m.run('BUY-B')
        m.run('BUY-B')
        self.assertEqual(m.b_items, 4)
        # self.assertEqual(m.response, ['Not enough money'])


if __name__ == '__main__':
    unittest.main()
