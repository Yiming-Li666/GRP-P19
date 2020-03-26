# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:43:25 2020

@author: user
"""

class CommonHelper:
    @staticmethod
    def readQSS(file_path, obj):
        with open(file_path,"r") as f:
            content = f.read()
            obj.setStyleSheet(content)