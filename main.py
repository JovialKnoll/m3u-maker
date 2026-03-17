#!/usr/bin/env python3

import argparse
import os
import sys

import m3u


MUSIC_TYPES = ('flac', 'm4a', 'mp3', 'ogg', 'wav', 'wma')

def main(dir: string):
    for root, dirs, files in os.walk(dir):
        if any(f.endswith('.m3u') for f in files):
            continue
        music_files = [
            f
            for f in files
            if f.endswith(MUSIC_TYPES)
        ]
        if music_files:
            m3u.make_m3u(root)


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
