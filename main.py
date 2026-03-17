#!/usr/bin/env python3

import argparse
import os
import sys


def main(dir: string):
    print(dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    args = parser.parse_args()
    dir = args.dir or os.getcwd()
    if not os.path.exists(dir):
        raise ValueError('dir passed in must exist')
    try:
        main(dir)
    except KeyboardInterrupt:
        pass
sys.exit()
