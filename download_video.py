import argparse
from pytube import YouTube

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="youtube video link",type=str)
args = parser.parse_args()

if (args.url):
    youtube = YouTube(args.url)

    video = youtube.streams.first()

    video.download('download')

    print("download video : " + video.title + " success!")
else:
    print("Error")
    parser.print_help()