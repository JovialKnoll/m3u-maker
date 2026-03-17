#!/usr/bin/env python3

import argparse
import os
import sys

import m3u


def main(dir: string):
    for root, dirs, files in os.walk(dir):
        # skip if .m3u already exists
        if any(f.endswith('.m3u') for f in files):
            continue
        music_files = m3u.get_music_files(files)
        # skip if only one or no music files
        if len(music_files) <= 1:
            continue
        lower_music_exists = False
        for root_in, dirs_in, files_in in os.walk(root):
            if root_in == root:
                continue
            music_files_in = m3u.get_music_files(files_in)
            if music_files_in:
                lower_music_exists = True
                break
        # skip if there are subdirectories with music files
        if lower_music_exists:
            continue
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
