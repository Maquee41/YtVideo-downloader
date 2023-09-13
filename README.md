# YtVideo Downloader
## Description

This script can download all videos from YouTube. To start you need only `yt-dlp` and `FFmpeg`

## Supported Resolution

| 2160p | 1440p | 1080p | 720p | 480p | 360p | 240p | 144p |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |

Check supported resolution in the quality tab (not all videos support all resolutions in YouTube)

![Alt text](https://user-life.com/uploads/posts/2021-06/1624555852_kak-izmenit-kachestvo-video-na-youtube3.png)


## Installation

1. Create new folder. Move there `main.py`
2. Install [FFmpeg](https://ffmpeg.org/)  If you use Windows you need only `ffmpeg.exe`. Find it in `\ffmpeg**version**\bin\` and move to a folder with main.py. If you use Linux install ffmpeg via terminal 'sudo apt install ffmpeg'
3. Create virtual environment
4. Download yt-dlp | `pip install yt-dlp`
5. That's all. Remember! you can use it only with Python interpreter

## CMD interface

- At first you should enter your video link
- Then you write your future video title
- And the last you can choose resolution  
example: `Select resolution 2160/1440/1080/720/480/360/240/144: 1080`)
