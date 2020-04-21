#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.cnblogs.com/rnckty/p/7722603.html
# 用这个实现跨文件全局变量，可以把TEACHERID存在这里，也可以临时存储LESSONID和MODULEID


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
