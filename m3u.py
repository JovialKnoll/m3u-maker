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
    print(dir)
    files = [
        f
        for f in os.listdir(dir)
        if os.path.isfile(os.path.join(dir, f))
    ]
    music_files = get_music_files(files)
    print(music_files)
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    args = parser.parse_args()
    dir = args.dir or os.getcwd()
    if not os.path.exists(dir):
        raise ValueError('dir passed in must exist')
    make_m3u(dir)
    sys.exit()
