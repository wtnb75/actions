import unittest
import dummy.main


class TestMain(unittest.TestCase):
    def test_main(self):
        res = dummy.main.main()
        self.assertEqual("world", res)
