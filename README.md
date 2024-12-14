# Video-to-audio-converter
A python script to convert video files into mp3 audio files.


### Requirements:


##### This script needs Python 3+ and ffmpeg, lame packages

If you don't have <b>Python 3</b> installed:

```bash
$ sudo apt-get install python3
```
If you don't have <b>ffmpeg</b> installed:

```bash
$ sudo apt-get install ffmpeg
```
If you don't have <b>lame</b> installed:

```bash
$ sudo apt-get install lame
```


### Clone:
```bash
$ git clone https://github.com/the-ahmadov/Video-to-audio-converter
$ cd ../Video-to-audio-converter
```

### Usage:

For single file
```bash
$ python3 video_to_audio.py <filename>
```

For all files in given folder name 
```bash
$ python3 video_to_audio.py <folder name>
```

Resulted audio files are saved in "audio" folder in the py file folder.
