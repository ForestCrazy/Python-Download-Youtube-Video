import argparse
import re
from pytube import *

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="youtube video link",type=str)
args = parser.parse_args()

if (args.url):
    pl = Playlist(args.url)

    pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print('Number of videos in playlist: %s' % len(pl.video_urls))

    for url in pl.video_urls:

        youtube = YouTube(url)

        video = youtube.streams.first()

        video.download('download')

        print("download video : " + video.title + " success!")

    print("download playlist : " + args.url + " success!")
else:
    print("Error")
    parser.print_help()