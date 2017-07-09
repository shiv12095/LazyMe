#!/usr/bin/python
# -*- coding: utf-8 -*-

from youtube.search import get_video_urls
from youtube.download import download_audio
from utilities.file_utilities import read_file

def main():
    songs = read_file("songs.txt")
    urls = get_video_urls(songs)
    download_audio(urls);

if __name__ == "__main__":
    main()
