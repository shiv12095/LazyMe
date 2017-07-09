#!/usr/bin/python
# -*- coding: utf-8 -*-

import pafy
import os
from pydub import AudioSegment

def download_audio(queries):
    for query in queries:
        m4a_audio_file = query["title"] + ".m4a"
        mp3_audio_file = query["title"] + ".mp3"
        video = pafy.new(query["url"])
        bestaudio = video.getbestaudio()
        bestaudio.download(quiet=False, filepath=m4a_audio_file)
        AudioSegment.from_file(m4a_audio_file).export(mp3_audio_file, format="mp3")
        os.remove(m4a_audio_file)
