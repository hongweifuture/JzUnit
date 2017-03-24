#!/usr/bin/env python
#coding=utf-8

"""
FuncName: JzClean.py
Desc: clean cache
Date: 2016-11-03 10:30
home: http://blog.csdn.net/z_johnny
Author: johnny
"""
import os

class JzClean(object):
    def __init__(self,pyc_path):
        self.pyc_path = pyc_path

    def cleanPyc(self):
        ''' Auto create .pyc and del it '''
        # Del all pyc in the current directory
        for pycpath, pycfolder, pycname in os.walk(self.pyc_path):
            for pyccase in pycname:
                if pyccase.endswith(".pyc"):
                    os.remove(os.path.join(pycpath, pyccase))

if __name__ == '__main__':
    pyc_path = os.getcwd()
    JzClean = JzClean(pyc_path)
    JzClean.cleanPyc()
