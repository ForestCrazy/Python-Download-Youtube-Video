from pytube import YouTube

url= 'https://youtu.be/u-GJBlpLoDE?list=RDu-GJBlpLoDE';

youtube = YouTube(url)

video = youtube.streams.first()

video.download('download')

print("download video : " + video.title + " success!")