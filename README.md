# Python-Download-Youtube-Video

## :arrow_down: Install pytube
```
pip install pytube # python2
pip3 install pytube # python3
pip install pytube3 # if not work with pytube.
```

## :arrow_forward: How to run
* Clone the repository: <br>
``` git clone https://github.com/ForestCrazy/Python-Download-Youtube-Video.git ```

* cd into directory into your command prompt: <br>
``` cd Python-Download-Youtube-Video ```

* Run the download_video.py file: <br>
``` python download_video.py --url "url_youtube_video" ```

* If you want to download the playlist then run the download_playlist.py: <br>
``` python download_playlist.py --url "url_youtube_playlist" ```

## :heavy_exclamation_mark: Fix Error
```
Traceback (most recent call last):
  File "C:\Python36-64\lib\site-packages\pytube\extract.py", line 297, in apply_descrambler
    for format_item in formats
  File "C:\Python36-64\lib\site-packages\pytube\extract.py", line 297, in <listcomp>
    for format_item in formats
KeyError: 'url'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "download_video.py", line 10, in <module>
    youtube = YouTube(args.url)
  File "C:\Python36-64\lib\site-packages\pytube\__main__.py", line 92, in __init__
    self.descramble()
  File "C:\Python36-64\lib\site-packages\pytube\__main__.py", line 132, in descramble
    apply_descrambler(self.player_config_args, fmt)
  File "C:\Python36-64\lib\site-packages\pytube\extract.py", line 301, in apply_descrambler
    parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
  File "C:\Python36-64\lib\site-packages\pytube\extract.py", line 301, in <listcomp>
    parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
KeyError: 'cipher'
```

1. Go to the location where the package was installed. If you don't know where, run the command <br>
``` pip show pytube3 ``` <br>
And it'll give you something like this: <br>
<img src="https://www.img.in.th/images/0ad7211653b048873b2c84951b6a2704.png" alt="pip show pytube3"><br>
We can see ``` Location: c:\python36-64\lib\site-packages ```

2. Go to that location, open the folder pytube and the file extract.py <br>
<img src="https://www.img.in.th/images/1ba4b5ef61670de584fd7bdf35bc573b.png" alt="folder pytube"><br>

3. In the file, line no. 306 or 301, you will find ``` parse_qs(formats[i]["cipher"])```. If yes, then change ``` "cipher" ``` to ``` "signatureCipher" ```
So, you'll initially have
```
cipher_url = [
                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
            ]
```
but it should be
```
cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]
```
