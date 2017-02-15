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
                    subprocess.call(['ffmpeg', '-i', i]) # placeholder, so insert anything else but this
                    shutil.move(os.path.join(dirname, i), os.path.join(dirname, 'completed'))
        time.sleep(10)


def main():
    try:
        os.makedirs(os.path.join(sys.argv[1], 'completed'))
    except:
        OSError
    check(sys.argv[1])


if __name__ == '__main__':
    main()
