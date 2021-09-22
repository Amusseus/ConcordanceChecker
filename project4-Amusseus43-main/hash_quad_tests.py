import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 10)
        ht.insert("biggerthaneightvalues", 1)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.get_value("notinhash"), None)
        self.assertEqual(ht.get_value("cat"), [5,10])

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("qat", 5)
        ht.insert("qat", 10)
        self.assertTrue(ht.in_table("qat"))
        self.assertFalse(ht.in_table("fgsdgfsdjhgfjdshfs"))
        self.assertEqual(ht.get_value("cat"), [5])

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("fghdgfdhgfd","A")
        ht.insert("fghdgfdhgfd","a")
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0) #causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)


if __name__ == '__main__':
   unittest.main()
