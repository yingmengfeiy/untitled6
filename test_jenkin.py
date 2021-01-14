# -*- coding: utf-8 -*-
"""
 @Software: PyCharm
 @File: test_jenkin.py
 @Author: hjp
 @Site: 
 @Time: 1月 14, 2021
"""


def setup_function():
    print("setup_function():每个方法之前执行")


def teardown_function():
    print("teardown_function():每个方法之后执行")


def test_01():
    print("正在执行test1")
    x = "this"
    assert 'h' in x


def test_02():
    print("正在执行test2")
    x = "hello"
    assert hasattr(x, "hello")
