#-*-coding:utf-8-*-
import os

myRoot = '/home/lufo/lufo816.github.com/'
from_ = 'categories'
to_ = 'tags'

def change(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            myFile = os.path.join(root, f)
            f = open(myFile, 'r')
            data = f.read()
            data = data.replace(from_, to_)
            f.close()
            f = open(myFile, 'w')
            f.write(data)
            f.close()

change(myRoot)
