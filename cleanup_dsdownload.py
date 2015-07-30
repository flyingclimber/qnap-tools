#!/usr/bin/python
'''
    cleanup.py - Remove .dsdownload extension from files in current tree
    '''

import os

EXT = '.dsdownload'
SRC_DIR = os.getcwd()

for root, dirs, files in os.walk(SRC_DIR, False):
    for name in files:
        if name.endswith(EXT):
            new_name = name.strip(EXT)
            src_file = root + "/" + name
            dst_file = root + "/" + new_name
            os.rename(src_file, dst_file)
        else:
            continue