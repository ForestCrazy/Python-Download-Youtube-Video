from pytube import YouTube

url = 'https://youtu.be/u-GJBlpLoDE?list=RDu-GJBlpLoDE'

youtube = YouTube(url)

#To list only audio streams:
print(youtube.streams.filter(adaptive=True))

#To list only mp4 streams:
print(youtube.streams.filter(subtype='mp4'))