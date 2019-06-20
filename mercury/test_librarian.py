# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""

import unittest
from mercury import librarian


class TestBorrower(unittest.TestCase):

    def test_import(self):
        librarian.Borrower();
        assert(True)