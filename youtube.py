import pytube
from pytube import YouTube
from pytube.cli import on_progress

url = 'https://www.youtube.com/watch?v=8lrfKGrsfuc'

yt = YouTube(url, on_progress_callback=on_progress)

# https://www.youtube.com/watch?v=8lrfKGrsfuc

# yt.streams.order_by('resolution').desc()

download_path = '/video'

yt = yt.streams.get_highest_resolution().download(download_path)
