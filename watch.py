#!/usr/bin/env python

import sys
import os
import subprocess
import time
import shutil

def check(dirname):
    while True:
        ls = os.listdir(dirname)
        if len(ls) > 0:
            for i in ls:
                if os.path.isfile(os.path.join(dirname,i)):
                    print i, 'found!'
                    statinfo = os.stat(os.path.join(dirname, i))
                    size = statinfo.st_size
                    time.sleep(10)
                    statinfo = os.stat(os.path.join(dirname, i))
                    while statinfo.st_size > size:
                        print 'checking if file is still transferring'
                        size = statinfo.st_size
                        time.sleep(10)
                        statinfo = os.stat(os.path.join(dirname, i))

                    subprocess.call(['ffmpeg', '-i', os.path.join(dirname,i)])
                    try:
                        shutil.move(os.path.join(dirname, i), os.path.join(dirname, 'completed'))
                    except shutil.Error:
                        shutil.move(os.path.join(dirname, i), os.path.join(dirname, 'completed/_%s_' % i))
        time.sleep(10)

def main():
    try:
        os.makedirs(os.path.join(sys.argv[1], 'completed'))
    except:
        OSError
    check(sys.argv[1])
if __name__ == '__main__':
    main()
