#!/usr/bin/env python3

import argparse
import os
import sys


MUSIC_TYPES = ('flac', 'm4a', 'mp3', 'ogg', 'wav', 'wma')


def get_music_files(files):
    return [
        f
        for f in files
        if f.endswith(MUSIC_TYPES)
    ]


def make_m3u(dir: string):
    # todo: make and save m3u file
    # check against track number of files to ensure order is right
    files = [
        f
        for f in os.listdir(dir)
        if os.path.isfile(os.path.join(dir, f))
    ]
    music_files = get_music_files(files)
    if not music_files:
        print("no music files here, exiting")
        return
    music_files.sort()
    m3u_file = os.path.join(dir, os.path.basename(dir) + '.m3u8')
    print(m3u_file)
    with open(m3u_file, 'w', encoding='utf-8') as f:
        for music_file in music_files:
            print(music_file, file=f)


def main(dir: string):
    for root, dirs, files in os.walk(dir):
        # skip if .m3u already exists
        if any(f.endswith('.m3u8') for f in files):
            continue
        music_files = get_music_files(files)
        # skip if only one or no music files
        if len(music_files) <= 1:
            continue
        lower_music_exists = False
        for root_in, dirs_in, files_in in os.walk(root):
            if root_in == root:
                continue
            music_files_in = get_music_files(files_in)
            if music_files_in:
                lower_music_exists = True
                break
        # skip if there are subdirectories with music files
        if lower_music_exists:
            continue
        make_m3u(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--single', action='store_true', help="just run on this directory")
    parser.add_argument('dir', help="the directory to run on")
    args = parser.parse_args()
    dir = args.dir.rstrip('"\\/')
    if not os.path.exists(dir):
        raise ValueError("directory passed in must exist")
    f = make_m3u if args.single else main
    try:
        f(dir)
    except KeyboardInterrupt:
        pass
    sys.exit()
