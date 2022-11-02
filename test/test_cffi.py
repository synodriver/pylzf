"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""
import sys
from random import choice, randint
from unittest import TestCase

sys.path.append(".")
import os

os.environ["LZF_USE_CFFI"] = "1"

from pylzf import LZF_VERSION, compress, decompress


class TestAll(TestCase):
    def setUp(self) -> None:
        pass

    def test_encode(self):
        for i in range(1000):
            data = bytes([randint(0, 255) for _ in range(randint(100, 1000))])
            out = compress(data, 2000)
            self.assertEqual(decompress(out, 1000), data)
        pass

    def test_version(self):
        self.assertEqual(LZF_VERSION, 261)

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    import unittest

    unittest.main()
