#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: testa.py
# @time: 2021/3/29 16:59
# @desc:
import unittest
class testa(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.a=1
        print('setUpClass')

    def setUp(self) -> None:
        print('setUp_%d'%self.a)

    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def test_01(self):
        print('test_01%d'%self.a)

    def test_02(self):
        print('test_02')

if __name__=='__main__':
    unittest.main()

