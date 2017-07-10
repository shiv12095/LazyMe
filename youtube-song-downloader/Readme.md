## YOUTUBE SONG DOWNLOADER
A simple python module to download songs from youtube. The module internally uses:
  - [pafy](https://github.com/mps-youtube/pafy)
  - [youtube-dl](https://rg3.github.io/youtube-dl/)
  - [pydub](https://github.com/jiaaro/pydub)

#### SETUP

1. Create / use your existing Google API developer keys and update them in `apiKey.json`. The developer keys can be obtained  [here](https://console.developers.google.com/apis/credentials)

2. Install the required python modules. Run the command

        pip install requirements.txt

#### USAGE
Update `songs.txt` with the list of songs that you want to download and execute

        python main.py
