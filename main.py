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


def make_m3u(directory: string):
    # check against track number of files to ensure order is right
    files = [
        f
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
    music_files = get_music_files(files)
    if not music_files:
        print("no music files here, exiting")
        return
    music_files.sort()
    m3u_file = os.path.join(directory, os.path.basename(directory) + '.m3u8')
    print(m3u_file)
    with open(m3u_file, 'w', encoding='utf-8') as f:
        for music_file in music_files:
            escaped_file = music_file.replace('#', '%23')
            print(escaped_file, file=f)


def main(directory: string, force: bool):
    for root, dirs, files in os.walk(directory):
        # skip if .m3u already exists
        if any(f.endswith('.m3u8') or f.endswith('.m3u') for f in files) and not force:
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
    parser.add_argument('-f', '--force', action='store_true', help="replace existing .m3u8 files")
    parser.add_argument('dir', help="the directory to run on")
    args = parser.parse_args()
    directory = args.dir.rstrip('"\\/')
    if not os.path.exists(directory):
        raise ValueError("directory passed in must exist")
    try:
        if args.single:
            make_m3u(directory)
        else:
            main(directory, args.force)
    except KeyboardInterrupt:
        pass
    sys.exit()
