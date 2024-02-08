import datetime
import time
import unittest

from jstimer4py import set_timeout


class TestJsTimer4Py(unittest.TestCase):
    def test_set_timeout(self):
        print(datetime.datetime.now())
        set_timeout(lambda: print(datetime.datetime.now()), 0)


if __name__ == '__main__':
    unittest.main()
