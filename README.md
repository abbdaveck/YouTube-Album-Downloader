# YouTube album downloader

This is a script that enables easy download of a Youtube song, playlist, album, EP or whatever.

## How does it work

The user start by pasting the url when asked for it. The scirpt then downloads the low quality mp4 version, converts it to mp3, adds the metadata and the album art. If the song is part of a playlist then the script downloads the rest of the playlist and moves all the song into a folder with the name of the album.

To download a playlist you need to paste a link that looks like this:
https://www.youtube.com/watch?v=rnZQvgWhM5s&list=OLAK5uy_lCQIipymSm8jFCYtkwOMZ84L3EgjqGfdk&index=1

To download just a song you past a link that looks like this:
https://www.youtube.com/watch?v=rnZQvgWhM5s

## IMPORTANT
Before you start the script you need to download all the neccesary libraries (youtube_dl, eyed3, Pil and moviepy). But you also need to right click on "download" on line 54 and click "Go to Definition". On line 2029 after "return self._download_retcode" add ", res". As far as I know this only works in Visual Studio

## Author

* **David Eckemark** - [abbdaveck](https://github.com/abbdaveck)

