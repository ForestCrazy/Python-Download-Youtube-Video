import re
from pytube import *

url = "https://www.youtube.com/watch?v=lx7LcOXPP8w&list=PLcbUOvrrEOny8FpktkPwKcZON33hwC5Rb"

pl = Playlist(url)

pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print('Number of videos in playlist: %s' % len(pl.video_urls))

for url in pl.video_urls:

    youtube = YouTube(url)

    video = youtube.streams.first()

    video.download('download')

    print("download video : " + video.title + " success!")

print("download playlist : " + url + " success!")